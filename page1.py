import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from huggingface_hub import InferenceClient
import os
import plotly.graph_objects as go
from dotenv import load_dotenv


import os
load_dotenv()



max_score = 100
client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("API_KEY"),
)


st.subheader("Context Similarity Between Text", divider="gray")
st.set_page_config(layout="wide")


def similarity_between_sentences(original_txt,test_txt):
    """
    This function takes input as two strings Main Text and Test Text and compute the different types of similarity between them.
    """
    result =client.sentence_similarity(original_txt,
    other_sentences=[test_txt],)

    return result[0]

  
def display(score):
    fig = go.Figure(go.Pie(
    values=[score, 100 - score],
    hole=0.7,
    marker_colors=["green", "lightgray"],
    textinfo="none",))

    fig.update_layout(
        showlegend=False,
        annotations=[dict(text=f"{score}%", x=0.5, y=0.5, font_size=24, showarrow=False)]
    )

    #st.write("### Your Score")
    st.plotly_chart(fig, use_container_width=True)


col1, col2= st.columns(2)

with col1:
    #st.header("Main Text")
    original_txt = st.text_area("original Text",height=300,disabled=False,key='original_txt',placeholder ="Please Insert The Main Text...")
with col2:
    #st.header("Test Text")
    test_txt = st.text_area("Test Text",height=300,disabled=False,key='test_txt',placeholder ="Please Insert Test Text...")
    

if original_txt and test_txt:
    similarity_score = similarity_between_sentences(original_txt,test_txt)
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>🏆 Your Final Score</h2>", unsafe_allow_html=True)
    _= display(int(similarity_score*100))





