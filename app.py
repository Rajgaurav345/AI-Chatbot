import streamlit as st
from chatbot import chatbot_response

st.set_page_config(page_title="AI Chatbot")

st.title("🤖 AI Chatbot")
st.caption("Built with Python, NLTK and Streamlit")

st.write("Ask me something!")

user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        response = chatbot_response(user_input)
        st.success(response)
