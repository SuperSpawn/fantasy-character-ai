import streamlit as st
from langchain.prompts import PromptTemplate

from template_strings.inspiration import inspiration_template


def set_inspiration_prompt():
    st.session_state['inspiration_prompt'] = PromptTemplate(
        template=inspiration_template,
        input_variables=['special_request'])


__all__ = ['set_inspiration_prompt']
