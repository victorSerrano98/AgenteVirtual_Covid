import streamlit as st
import requests, json
from annotated_text import annotated_text
import os
from googletrans import Translator
translator = Translator()


qa_ip = os.environ.get('qa_ip', 'https://fastapitesis-m36rwfdc5q-uc.a.run.app')
qa_port = os.environ.get('qa_port', '85')


st.set_page_config(
    page_title="Chatbot",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
    )

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    
def icon(icon_name):
    st.markdown(f'<i class="fa fa-external-link" aria-hidden="true"></i>', unsafe_allow_html=True)

remote_css("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

st.markdown('<h1 style="text-align: center">Agente Conversacional</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center">Universidad Nacional de Loja</h3>', unsafe_allow_html=True)

st.sidebar.header("Opciones")
top_k_reader = st.sidebar.slider("Numero de Respuestas", min_value=1, max_value=10, value=1, step=1)
top_k_retriever = st.sidebar.slider("Numero de documentos", min_value=1, max_value=10, value=1, step=1)


st.markdown('<h3>Pregunta: </h3>', unsafe_allow_html=True)
question_es = st.text_input("Ingrese su pregunta", value="¿Cuáles son los síntomas del covid-19?")

button = st.button('Buscar')
st.text("")
st.text("")

if button:
    question = translator.translate(question_es, 'en')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    data = {
         'question': question.text, 'num_answers': top_k_reader, 'num_docs': top_k_retriever
    }


    try:
        response = requests.post(f'https://fastapitesis-m36rwfdc5q-uc.a.run.app/query', headers=headers, data=json.dumps(data))
        result = response.json()


        for each in result['answer']['answers']:
            title = each['meta']['title']
            url = each['meta']['url'].split(';')[0]
            tokens = []
            respuesta = translator.translate(each['context'][:each['offset_start']-1], dest='es')
            tokens.append(respuesta.text)
            respuesta = translator.translate(each['context'][each['offset_start']:each['offset_end']], dest='es')
            tokens.append((respuesta.text,'ANS', '#BAF2A2'))
            respuesta = translator.translate(each['context'][each['offset_end']:], dest='es')
            tokens.append(respuesta.text)
            col1,col2 = st.beta_columns([5,1])
            col1.markdown(f'<span style="font-size: 16; font-weight:bold;">{title}</span><a href={url} target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>', unsafe_allow_html=True)
            col2.markdown(f'<input type="button" value="Confianza: {int(each["probability"]*100)}%">', unsafe_allow_html=True)
            st.text("")
            col1, col2 = st.beta_columns([2,4])
            col1.markdown(f'<span style="font-size: 16; font-weight:bold;">Fecha de Publicacion: {each["meta"]["publish_time"]}\
                        <br>Autores: {each["meta"]["authors"]}</span>', unsafe_allow_html=True)
            annotated_text(*tokens)
            st.text("")
            st.text("")
        
    except:
        col1,col2 = st.beta_columns([5,1])
        st.error("Ha ocurrido un error, vuelva a intentarlo")
        st.text("")
        col1, col2 = st.beta_columns([2,4])

    