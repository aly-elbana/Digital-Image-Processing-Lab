import streamlit as st
from utils.state_manager import get_messages, set_messages
from processing.assistant import generate_bot_response

def main() -> None:
    st.set_page_config(page_title="Your Assistant", page_icon="🤖", layout="centered")
    st.title("Your Assistant")

    if not get_messages():
        set_messages([])

    for msg in get_messages():
        role = "assistant" if msg["role"] == "bot" else msg["role"]
        with st.chat_message(role):
            st.markdown(msg["content"])

    if user_input := st.chat_input("Write a message..."):
        
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            full_response = st.write_stream(generate_bot_response(user_input))
        

        current_messages = get_messages()
        current_messages.append({"role": "user", "content": user_input})
        current_messages.append({"role": "assistant", "content": full_response})
        set_messages(current_messages)

if __name__ == "__main__":
    main()