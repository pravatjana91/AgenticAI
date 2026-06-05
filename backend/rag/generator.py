import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

OLLAMA_API_URL = "http://localhost:11434/api/generate"


def generate_response(query,context):

    if context is None:
        return "No relevant information found."

    context_text = "\n\n".join(context)
    
    prompt = f"""Answer the question in maximum 3 sentences.

Use only the provided context.

If the answer is not in the context, say:
"I could not find relevant information."

Context:
{context_text}

Question:
{query}"""

    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(OLLAMA_API_URL, json=payload)
    response_data = response.json()
    

    print(response_data)

    return response_data.get("response", "Error generating response")

    