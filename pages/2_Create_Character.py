# Write a basic draft version of the character

import streamlit as st
from reset.reset import reset
from templates.set_parser import set_parser

reset()

if not st.session_state['prompt_template']:
    set_parser()

st.title("Character")

if not st.session_state['prompt_template']:
    submit_button_disabled = True
else:
    submit_button_disabled = False

with st.form(key="character_form", clear_on_submit=False):
    description = st.text_area(label="Character description:",
                               value=st.session_state['default_description'],
                               placeholder="example: brave orc warrior...")
    if st.form_submit_button("Submit", disabled=submit_button_disabled):
        _input = st.session_state['prompt_template'].format_prompt(
            description=description, parameters=st.session_state['string_parameters'])
        output = st.session_state['llm'](_input.to_string())
        st.session_state['character'] = output
        st.success("Successfully created character")

st.write(st.session_state['character'])

st.divider()
# st.write("")
special_request = st.text_input(
    "Special Request:", placeholder="e.g. funny character")
if st.button("Generate suggestion"):
    _input = st.session_state['inspiration_prompt'].format_prompt(
        special_request=special_request)
    st.session_state['default_description'] = st.session_state['llm'](
        _input.to_string())
