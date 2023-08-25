import streamlit as st
from reset.reset import reset

reset()

st.title("Chat with character")


chat_disabled = st.session_state['character'] == ""

prompt = st.chat_input("Your message", disabled=chat_disabled)
if prompt:
    response = st.session_state['chat_llm']({
        'user_input': prompt})
    with st.chat_message("character"):
        st.write(response['text'])
