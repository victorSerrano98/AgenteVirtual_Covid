# Agente virtual para brindar asistencia acerca del Covid-19
<p></p>
Agente virtual desarrollado con el modelo de lenguaje BERT, el cual fue previamente afinado para responder preguntas comunes del covid-19.
<p></p>
<div align="center">
	 <img src ="https://user-images.githubusercontent.com/33547749/159361179-e5cae02e-8a26-42cc-acb7-e1c4a0401e1f.png" width="600" height="350" />
</div>
<p></p>
 
<b>Autores:</b>
	Victor Yamil Serrano Zari,  José Alexis Carrión Ojeda

# Introducción
En este repositorio se encuentran los archivos utilizados para el desarrollo del trabajo de titulacion "Agente virtual para brindar asistencia acerca del Covid-19", se encuentra divido en carpetas en las cuales se pueden encontrar los archivos que fueron necesarios para el ajuste de modelo BERT, la creacion de la base conocimientos utilizando Elasticsearch, la Api con ayuda del frameword FastApi y la interfaz desarrollada con Elasticsearch.

# librerias utilizadas
<A HREF="https://huggingface.co/bert-base-uncased">BERT: </A> es un modelo de representación de lenguaje, que significa Representaciones de codificador bidireccional de Transformers. Está diseñado para entrenar representaciones bidireccionales profundas a partir de texto sin etiquetar a través de una capa contextual, que se compone de capas de atención apiladas y redes de retroalimentación con incorporaciones de entrada y salida de la secuencia.
<p></p>
<A HREF="https://pytorch.org/"> Pytorch: </A>   es una biblioteca de tensores optimizada para el aprendizaje profundo mediante GPU y CPU, proporciona dos funciones de alto nivel: Cálculo de tensor (como NumPy) con fuerte aceleración de GPU y Redes neuronales profundas construidas en un sistema de autogrado basado en cintas.
<p></p>
<A HREF="https://haystack.deepset.ai/overview/intro">Haystack: </A>  Es un framework de Python para el desarrollo de sistemas de búsqueda en grandes colecciones de documentos, está disponible como una biblioteca de código abierto que proporciona diferentes aplicaciones entra las que destaca la recuperación de respuestas a preguntas.
<p></p>
<A HREF="https://fastapi.tiangolo.com/">FastAPI: </A> Se trata de un framework que permite construir APIs (Application Programming Interfaces o Interfaz de programación de aplicaciones) de forma rápida con Python, con la finalidad intercambiar datos entre los distintos módulos de un sistema.
<p></p>
<A HREF="https://www.elastic.co/es/">Elasticserch: </A> es un motor de búsqueda y recuperación de documentos de tipo JSON basado en Apache Lucene, el cual permite realizar búsquedas por una gran cantidad de datos de un texto específico.
<p></p>
<A HREF="https://streamlit.io/">Streamlit: </A> Es un framework de creación de aplicaciones de código abierto y gratuito creado para proyectos de aprendizaje automático y ciencia de datos, esta herramienta basada en Python permite crear aplicaciones web en tiempo real mientras se va codificando, sin la necesidad de saber HTML o CSS, permite la integración de Bootstrap y crea una interfaz interactiva y amigable con los usuarios.
