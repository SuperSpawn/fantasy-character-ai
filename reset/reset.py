import streamlit as st
import json
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from templates.set_inspiration_prompt import set_inspiration_prompt
from template_strings.chat_character import get_chat_character_template


def reset():
    with open("./data/parameters.json") as file:
        data = json.load(file)
    if 'parameters' not in st.session_state:
        st.session_state['parameters'] = data
    if 'prompt_template' not in st.session_state:
        st.session_state['prompt_template'] = None
    if 'llm' not in st.session_state:
        st.session_state['llm'] = OpenAI(temperature=0.7)
    if 'character' not in st.session_state:
        st.session_state['character'] = ""
    if 'default_description' not in st.session_state:
        st.session_state['default_description'] = ""
    if 'chat_llm' not in st.session_state:
        template = get_chat_character_template(st.session_state['character'])
        prompt = PromptTemplate(
            input_variables=['chat_history', 'user_input'],
            template=template)
        memory = ConversationBufferMemory(memory_key="chat_history")
        llm = OpenAI()
        llm_chain = LLMChain(
            llm=llm,
            prompt=prompt,
            verbose=True,
            memory=memory,
        )
        st.session_state['chat_llm'] = llm_chain
    set_inspiration_prompt()


__all__ = ['reset']
