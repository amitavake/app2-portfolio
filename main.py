import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/boater_pic.jpg")

with col2:
    st.title("Amitava Gangopadhyay")
    content="""
    Hi! I am Amitava. I am a Data Science leader. I have been working 
    on ML/DL/AI/Data Science in the IT industry for the last more than
    18 years. 
    """
    st.info(content)