import ollama
import json
import re


MODEL = "qwen3:4b"


def route_message(user_message, conversation_history):
    history_text = ""

    for message in conversation_history[-8:]:
        history_text += f'{message["role"]}: {message["content"]}\n'

    prompt = f"""
You are an intent router for an AI chatbot.

Your job is to understand what the user wants.

Possible intents:

- general_information
- pricing
- features
- details
- comparison
- recommendation
- current_information
- other

You must also determine the entity/topic being discussed.

Conversation history:
{history_text}

Current user message:
{user_message}

Return ONLY valid JSON.

Use exactly this format:

{{
    "intent": "one intent from the list",
    "entity": "main entity or topic",
    "search_required": true,
    "search_query": "best search query if search is required",
    "focus": "what the user specifically wants"
}}

Rules:

1. If the user asks about current pricing, search_required must be true.
2. If the user asks about current information, search_required must be true.
3. If the user asks about a company/product/service and accurate current information is useful, search_required can be true.
4. If the user asks a basic/general question that does not need current information, search_required can be false.
5. Resolve words like "it", "its", "this", "that plan" using conversation history.
6. Do not answer the user.
7. Return JSON only.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a strict JSON intent classifier."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"].strip()

    # Remove markdown code fences if Qwen adds them
    content = re.sub(r"```json", "", content)
    content = re.sub(r"```", "", content).strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        # Fallback if model returns malformed JSON
        return {
            "intent": "general_information",
            "entity": "",
            "search_required": False,
            "search_query": user_message,
            "focus": user_message
        }