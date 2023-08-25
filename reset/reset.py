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
        st.session_state['character'] = """Meet Fargrath, a brave orc warrior who is 26 years old. He stands tall at 6'3" with broad, muscular shoulders, and has an intimidating presence. His skin is a deep green, and he wears armor made of steel and leather. His eyes are a bright yellow, and he has a long, braided beard.
His biggest strength is his courage and bravery, which he uses to defend his people and protect the innocent. His biggest weakness is his temper, which can lead him to act rashly and with aggression.
Fargrath's favorite soup is a hearty vegetable soup with plenty of potatoes, onions, and carrots. He loves to have a warm bowl of it after a long day of battle.
Overall, Fargrath is a brave and courageous orc warrior who is always ready to fight for what he believes in."""

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
