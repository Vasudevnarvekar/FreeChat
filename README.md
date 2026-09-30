🤖 FreeChat AI — Intelligent Conversational Product Assistant

FreeChat AI is a dynamic, context-aware conversational AI assistant designed to understand natural-language user requests and determine what type of response or action is required.

Unlike a chatbot that relies on predefined commands such as /pricing, /features, or /compare, FreeChat AI allows users to communicate naturally.

For example:

User: Tell me about Netflix.
FreeChat: Provides an overview of Netflix.

User: What are its pricing plans?
FreeChat: Understands that "its" refers to Netflix and retrieves current pricing information.

User: Explain the Premium plan in detail.
FreeChat: Understands that the Premium plan belongs to Netflix and provides a detailed explanation.

User: Which plan is suitable for two people?
FreeChat: Uses the previous conversation context and plan characteristics to explain the relevant options.

The project combines LLM-based intent detection, conversational context, web search, and dynamic response generation to create a more intelligent chatbot experience.

📌 Project Overview

Traditional chatbots often depend on predefined commands or fixed flows:

User
 ↓
/pricing
 ↓
Pricing Function
 ↓
Pricing Response

FreeChat AI follows a different approach:

User Natural Language
        ↓
Conversation Context
        ↓
LLM Router
        ↓
Intent + Entity Detection
        ↓
Web Search (when required)
        ↓
LLM Response Generation
        ↓
Context-Aware Answer

The system dynamically determines what the user is asking instead of requiring the user to select a predefined function.

🎯 Problem Statement

Users should be able to ask questions naturally without knowing which command or function to use.

For example, a user may ask:

Tell me about ChatGPT

followed by:

What are its pricing plans?

followed by:

Explain the paid plans

and finally:

Which one would be suitable for me?

The chatbot should understand that all these questions are connected to the same conversation.

The main challenge is therefore:

How can an AI assistant understand arbitrary natural-language input, identify the user's intent and relevant entity, retrieve current information when necessary, and generate a context-aware response?

FreeChat AI addresses this problem using an LLM-powered routing and response-generation architecture.
