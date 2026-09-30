import streamlit as st
import ollama

from router import route_message
from web_search import search_web
from prompts import SYSTEM_PROMPT, build_response_prompt


MODEL = "qwen3:4b"


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="FreeChat AI",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# SESSION STATE
# -----------------------------

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hello! I'm FreeChat AI. Ask me anything."
        }
    ]


# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("🤖 FreeChat AI")

    st.write("Dynamic AI Assistant")

    if st.button("➕ New Chat", use_container_width=True):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "👋 Hello! I'm FreeChat AI. How can I help you today?"
            }
        ]

        st.rerun()

    st.divider()

    st.caption("Powered by Qwen3 + Ollama")


# -----------------------------
# MAIN UI
# -----------------------------

st.title("🤖 FreeChat AI")

st.caption(
    "Ask anything — pricing, features, products, companies, technologies, comparisons and more."
)


# -----------------------------
# DISPLAY CHAT
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# -----------------------------
# USER INPUT
# -----------------------------

user_message = st.chat_input(
    "Ask FreeChat anything..."
)


if user_message:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_message)

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })


    # -----------------------------
    # AI PROCESSING
    # -----------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # 1. ROUTER
            router_result = route_message(
                user_message,
                st.session_state.messages
            )

            # Debug information
            with st.expander("🔍 AI Decision", expanded=False):

                st.json(router_result)


            # 2. WEB SEARCH
            search_results = []

            if router_result.get("search_required"):

                search_results = search_web(
                    router_result.get(
                        "search_query",
                        user_message
                    )
                )


            # 3. BUILD RESPONSE PROMPT
            response_prompt = build_response_prompt(
                user_message,
                st.session_state.messages,
                router_result,
                search_results
            )


            # 4. GENERATE ANSWER
            response = ollama.chat(
                model=MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": response_prompt
                    }
                ]
            )


            answer = response["message"]["content"]


        # Display answer
        st.markdown(answer)


    # Save answer
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })