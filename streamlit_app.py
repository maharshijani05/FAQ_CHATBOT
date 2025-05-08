import streamlit as st
from faq_chatbot import run_faq_bot

st.set_page_config(page_title="FAQ Chatbot", page_icon="💬", layout="centered")

st.title("💬 FAQ Chatbot for BudgetPro")
st.markdown("Ask any question based on the FAQ document.")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = "user_1"  # Customize per user if needed

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask something...")
if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Run chatbot
    answer = run_faq_bot(user_input, session_id=st.session_state.session_id)

    # Display assistant response
    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
