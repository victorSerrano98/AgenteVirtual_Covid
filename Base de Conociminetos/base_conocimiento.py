
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document")

import pandas as pd 
df = pd.read_csv("D:\Tesis\FINAL_CORD_DATA2.csv")

print(df.head())

dicts = df.to_dict('records')

final_dicts = []
for each in dicts:
    tmp = {}
    tmp['text'] = each.pop('body_text')
    tmp['meta'] = each
    final_dicts.append(tmp)


document_store.write_documents(final_dicts)