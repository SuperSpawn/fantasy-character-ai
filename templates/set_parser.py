import streamlit as st
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate

from template_strings.character import character_template


def set_parser():
    params = "{\n"
    for param in st.session_state['parameters']:
        field = param['name'] + ": " + param['description']
        params += field + ",\n"
    params += "\n}"
    prompt = PromptTemplate(
        template=character_template,
        input_variables=['description', 'parameters']
    )
    st.session_state['prompt_template'] = prompt
    st.session_state['string_parameters'] = params


__all__ = ['set_parser']
