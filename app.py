import os
from dotenv import load_dotenv

import streamlit as st
from reset.reset import reset

# Load the .env file
load_dotenv()

# Set the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Verify the loaded key
if OPENAI_API_KEY:
    print("OPENAI_API_KEY loaded successfully!")
else:
    print("Failed to load OPENAI_API_KEY.")


reset()

st.title("Character maker AI")
