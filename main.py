import streamlit as st


with st.sidebar:
    st.markdown("## 👤 Contact Information")
    
    st.markdown("""
    <div style="line-height: 1; font-size: 13px;">
        <b>👨‍💼 Name:</b><br> Prathamesh Gangadhar Dyade<br><br>
        <b>📱 Contact:</b><br> <a href="tel:+919130639541" style="text-decoration: none; color: white;">+91 9130639541</a><br><br>
        <b>📧 Email:</b><br> <a href="mailto:prathameshdyade123@gmail.com" style="text-decoration: none; color: white;">prathameshdyade123@gmail.com</a><br><br>
        <b>🏢 Position:</b><br> ML Engineer, Alstom India<br><br>
        <b>🎓 Education:</b><br> M.Tech in AI & ML
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("🌐 [LinkedIn](https://www.linkedin.com/in/prathamesh-dyade-8030a21a9/) | 📁 [GitHub](https://github.com/prathmeshgd)")


def page2():
    st.title("Summarisation")

pg = st.navigation([
    st.Page("page1.py", title="Context Similarity", icon="🔥"),
    st.Page(page2, title="Summarisation", icon="📝"),
])
pg.run()

