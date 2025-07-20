import streamlit as st


def page2():
    st.title("Summarisation")

pg = st.navigation([
    st.Page("page1.py", title="Context Similarity", icon="🔥"),
    st.Page(page2, title="Summarisation", icon="📝"),
])
pg.run()

