# Configure character parameters

import streamlit as st
from reset.reset import reset

# Reset session
reset()


st.title("Parameters")

st.write("**Character parameters**:")

with st.form(key="create_parameter", clear_on_submit=True):
    # Input for new string
    param_name = st.text_input("Name:")
    param_description = st.text_input("Description:")

    # Button to add new string to the list
    if st.form_submit_button("Add to list"):
        if not param_description.endswith('.'):
            param_description += '.'
        param = {'name': param_name, 'description': param_description}
        st.session_state['parameters'].append(param)
        st.success("Successfully added")
        st.session_state['prompt_template'] = None

st.divider()

st.write("**Parameters:**")
edited_df = st.data_editor(st.session_state['parameters'])
st.session_state['parameters'] = edited_df

st.json(st.session_state['parameters'], expanded=False)

if st.button("Reset"):
    st.session_state['parameters'] = []
    st.session_state['prompt_template'] = None
