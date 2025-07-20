import streamlit as st
import numpy as np
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
            st.markdown("<h2 style='text-align: center; color: #4CAF50;'>🏆 Your Final Score</h2>", unsafe_allow_html=True)
            _= display(int(similarity_score*100))





