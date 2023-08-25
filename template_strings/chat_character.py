

def get_chat_character_template(description):
    return f"""
Based on the following character description, role play as the character in any subsequent interaction:

{{chat_history}}
Description: {description}
User: {{user_input}}
Character:
"""


__all__ = ['get_chat_character_template']
