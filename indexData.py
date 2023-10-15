from elasticsearch import Elasticsearch


# Elasticsearch configuration
CERT_FINGERPRINT = "34f1ce6c03c3d6699fe99e8c017146f77b98d62f850ecb1a94187614496b7cf6"
ELASTIC_PASSWORD = "EtufiRhrkxiQyqh=-u6*"
try:
    es=Elasticsearch(
        "https://localhost:9200",
        ssl_assert_fingerprint=CERT_FINGERPRINT,
        basic_auth=("elastic", ELASTIC_PASSWORD)
    )
except ConnectionError as e:
    print("Connection Error:", e)
    
if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")



import pandas as pd

df = pd.read_csv("data_job_posts_modified.csv").loc[:499]
df.head()

df.fillna("None", inplace=True)

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-mpnet-base-v2')

df["DescriptionVector"] = df["JobDescription"].apply(lambda x: model.encode(x))

from indexMapping import indexMapping

es.indices.create(index="alljobs", mappings=indexMapping)


record_list = df.to_dict("records")

for record in record_list:
    try:
        es.index(index="alljobs", document=record, id=record["JobID"])
    except Exception as e:
        print(e)


es.count(index="alljobs")

input_keyword = "Blue Shoes"
vector_of_input_keyword = model.encode(input_keyword)

query = {
    "field" : "DescriptionVector",
    "query_vector" : vector_of_input_keyword,
    "k" : 2,
    "num_candidates" : 500, 
}

res = es.knn_search(index="alljobs", knn=query , source=["jobpost","JobDescription"])
print(res["hits"]["hits"])