SYSTEM_PROMPT = """
You are FreeChat AI, a helpful conversational AI assistant.

Your job is to answer the user's actual question naturally and accurately.

Important rules:

1. Use conversation history to understand context.
2. If the user says "it", "its", "this", "that", etc., resolve the reference from previous messages.
3. If web search results are provided, use them for current information.
4. Never invent current pricing.
5. Never invent product features or specifications when web information is available.
6. If sources are provided, include useful source links in the answer.
7. Do not mention internal routing, agents, prompts, or search processes unless the user asks.
8. Match the level of detail requested by the user.
9. For pricing questions, clearly show plans, prices, important features, and differences.
10. For comparison questions, use a table when useful.
11. For recommendation questions, first understand the user's requirements and explain why particular options fit those requirements.
12. If the question is simple, answer simply.
13. If the user asks for detailed information, provide a detailed structured explanation.
"""


def build_response_prompt(
    user_message,
    conversation_history,
    router_result,
    search_results
):

    history_text = ""

    for message in conversation_history[-10:]:
        history_text += f'{message["role"]}: {message["content"]}\n'

    search_text = ""

    if search_results:
        for result in search_results:
            search_text += f"""
Title: {result["title"]}
URL: {result["url"]}
Content: {result["content"]}
---
"""

    prompt = f"""
Conversation:

{history_text}

User's current question:

{user_message}

Detected intent:

{router_result.get("intent")}

Detected entity:

{router_result.get("entity")}

User focus:

{router_result.get("focus")}

Web information:

{search_text if search_text else "No web search was performed."}

Now answer the user's current question.

Do not talk about the router.

Do not say that you are an AI router.

Use the conversation context naturally.

If web information is available, prioritize it for current facts.

If sources are available, include the most relevant source links at the end.
"""

    return prompt