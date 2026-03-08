import streamlit as st
import requests

API_SIMILARITY = "http://127.0.0.1:8000/similarity"
API_MULTIQUERY = "http://127.0.0.1:8000/multiquery"

st.title("RAG Search Application")

query = st.text_input("Enter your query")

if st.button("Similarity Search"):

    response = requests.post(
        API_SIMILARITY,
        json={"query": query}
    ).json()

    st.subheader("Similarity Results")

    for result in response["results"]:
        st.write(result)


if st.button("Multi Query Search"):

    response = requests.post(
        API_MULTIQUERY,
        json={"query": query}
    ).json()

    st.subheader("MultiQuery Results")

    for result in response["results"]:
        st.write(result)