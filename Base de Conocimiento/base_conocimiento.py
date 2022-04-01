
#importacion de paquetes 
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
#conexion con el contenedor de elasticsearch
document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document")

import pandas as pd 
df = pd.read_csv("D:\FINAL_CORD_DATA2.csv")

print(df.head())

#Convierte el DataFrame en un diccionario
dicts = df.to_dict('records')

final_dicts = []
for each in dicts:
    tmp = {}
    tmp['text'] = each.pop('body_text')
    tmp['meta'] = each
    final_dicts.append(tmp)

#Se agrega los documentos al contendor elasticsearch
document_store.write_documents(final_dicts)
