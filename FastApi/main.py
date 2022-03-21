#Importacion de paquetes
from elasticsearch import Elasticsearch
from fastapi import FastAPI
from pydantic import BaseModel

from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
import os
from haystack.pipeline import ExtractiveQAPipeline
from haystack.reader.farm import FARMReader
from haystack.retriever.sparse import ElasticsearchRetriever

#conexion con el contenedor de elasticsearch
ELASTIC_SEARCH_HOST =  os.environ.get('es_ip', 'host.docker.internal')
ELASTIC_SEARCH_PORT =  os.environ.get('es_port', 9200)

document_store = ElasticsearchDocumentStore(host=ELASTIC_SEARCH_HOST,
                                            port= ELASTIC_SEARCH_PORT,
                                            username="", password="",
                                            index="document")

#Se utiliza el modelo previamente afinado
retriever = ElasticsearchRetriever(document_store=document_store)
reader = FARMReader(model_name_or_path="JAlexis/PruebaBert", use_gpu=True)
pipe = ExtractiveQAPipeline(reader, retriever)

app = FastAPI()

class Queobj(BaseModel):
    question: str
    num_answers: int
    num_docs: int

@app.post('/query')
async def query(que_obj: Queobj):
    question = que_obj.question
    k_retriver = que_obj.num_docs
    k_reader = que_obj.num_answers
    prediction = pipe.run(query=question, top_k_retriever=k_retriver, top_k_reader=k_reader)
    return {'answer': prediction}
