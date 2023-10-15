import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "alljobs"

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



model = SentenceTransformer('all-mpnet-base-v2')
def search(input_keyword):
    global model
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "DescriptionVector",
        "query_vector": vector_of_input_keyword,
        "k": 10,
        "num_candidates": 500
    }
    res = es.knn_search(index=indexName
                        , knn=query 
                        , source=["jobpost","JobDescription"]
                        # source=["jobpost","JobDescription"]
                        )
    results = res["hits"]["hits"]

    return results

def main():
    st.title("Search Job descriptions")

    # Input: User enters search query
    search_query = st.text_input("Enter your search query")

    # Button: User triggers the search
    if st.button("Search"):
        if search_query:
            # Perform the search and get results
            results = search(search_query)

            # Display search results
            st.subheader("Search Results")
            for result in results:
                with st.container():
                    if '_source' in result:
                        try:
                            st.header(f"{result['_source']['jobpost']}")
                        except Exception as e:
                            print(e)
                        
                        try:
                            st.write(f"Description: {result['_source']['JobDescription']}")
                        except Exception as e:
                            print(e)
                        st.divider()

                    
if __name__ == "__main__":
    main()
