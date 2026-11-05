
import os

from google import genai


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable is missing")


client = genai.Client(
    api_key=GEMINI_API_KEY
)

MODEL = "gemini-3.6-flash"


def generate_answer(question, context, history=None):

    history_text = ""

    if history:
        for message in history[-6:]:
            role = message["role"]
            content = message["content"]

            history_text += f"{role}: {content}\n"

    prompt = f"""
You are DevDocs AI, a developer documentation assistant.

Answer the user's question using the documentation context
and relevant conversation history.

Rules:
- Do not invent documentation information.
- Use the provided documentation when answering technical questions.
- Use conversation history to understand follow-up questions.
- If the answer cannot be found in the documentation, say:
  "I couldn't find this information in the documentation."
- Give clear and concise developer-friendly answers.

Previous Conversation:
{history_text}

Documentation Context:
{context}

Current User Question:
{question}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text
