
import streamlit as st
from utils.app_utils import load_all_excels, answer_with_rag

st.set_page_config(page_title="Travel Chatbot — Tanushree Vaitage", page_icon="💬", layout="wide")

st.markdown("### 🔙 [Back to Home](../Home.py)")
st.header("Travel Chatbot")

if "data_cache" not in st.session_state:
    st.session_state["data_cache"] = load_all_excels("data")
data = st.session_state["data_cache"]

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for m in st.session_state["messages"]:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

prompt = st.chat_input("Ask about destinations, budgets, or itineraries...")
if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    answer = answer_with_rag(prompt, data)

    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state["messages"].append({"role": "assistant", "content": answer})
