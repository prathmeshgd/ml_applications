import streamlit as st
import numpy as np
from huggingface_hub import InferenceClient
import os
import plotly.graph_objects as go
from dotenv import load_dotenv
import time

import os
load_dotenv()



max_score = 100
client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("API_KEY"),
)


st.title("🔍 Text Similarity Checker")
st.markdown("---")

with st.container():
    st.subheader("📘 About the Application")
    st.markdown("""
    Welcome to the **Text Similarity Checker** app! 🧠✨

    This application helps you **analyze the similarity** between two pieces of text:
    
    - 🔹 **Original Text**: The source or reference content.
    - 🔹 **Test Text**: The text you want to compare.

    Using powerful Natural Language Processing (NLP) techniques and embeddings, the app calculates a **similarity score out of 100**, giving you quick insights into how close or different the two texts are.

    ---
    💡 Ideal for:
    - Plagiarism detection
    - Paraphrasing validation
    - Content matching
    - AI-generated text evaluation

    🚀 Try it out and see how similar your content really is!
    """)

st.subheader("Context Similarity Between Text", divider="gray")
st.set_page_config(layout="wide")


def similarity_between_sentences(original_txt,test_txt):
    """
    This function takes input as two strings Main Text and Test Text and compute the different types of similarity between them.
    """
    result =client.sentence_similarity(original_txt,
    other_sentences=[test_txt],)

    return result[0]

def get_color(score):
    """Return color based on score using soft border transitions."""
    if score <= 20:
        return "#FF4C4C"  # bright red
    elif score <= 40:
        return "#FF914D"  # orange-red
    elif score <= 60:
        return "#FFD700"  # yellow
    elif score <= 80:
        return "#9ACD32"  # yellow-green
    else:
        return "#2ECC71"  # green

def display(score):
    with st.spinner("🔍 Analyzing similarity... Please wait"):
        time.sleep(1.5)  # Simulated delay (you can remove or adjust this)

    color = get_color(score)

    fig = go.Figure(go.Pie(
        values=[score, 100 - score],
        hole=0.7,
        marker_colors=[color, "lightgray"],
        textinfo="none",
    ))

    fig.update_layout(
        showlegend=False,
        annotations=[
            dict(text=f"{score}%", x=0.5, y=0.5, font_size=26, showarrow=False),
            dict(
                text="Similarity Score between Your Texts",
                x=0.5, y=1.15, xref='paper', yref='paper',
                font_size=20, showarrow=False
            )
        ],
        margin=dict(t=80, b=0, l=0, r=0)
    )

    st.plotly_chart(fig, use_container_width=True)


col1, col2= st.columns(2)

with col1:
    #st.header("Main Text")
    original_txt = st.text_area("✍️Enter the original Text",height=300,disabled=False,key='original_txt',placeholder ="Please Insert The Main Text...")
with col2:
    #st.header("Test Text")
    test_txt = st.text_area("📝 Enter Test Tex",height=300,disabled=False,key='test_txt',placeholder ="Please Insert Test Text...")
    
with col2:
    analyze_clicked = st.button("🔎 Analyze",key='col2_button')

if analyze_clicked:
    if original_txt and test_txt:
        if analyze_clicked:
            similarity_score = similarity_between_sentences(original_txt,test_txt)
            st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Context Similirity</h2>", unsafe_allow_html=True)
            _= display(int(similarity_score*100))





