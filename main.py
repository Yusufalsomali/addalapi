from fastapi import FastAPI, Request
from groq import Groq
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to Lovable domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    messages = data.get("messages")

    if not messages or not isinstance(messages, list) or len(messages) == 0:
        return {"error": "Missing or invalid 'messages'. Must be a list with at least one message."}

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages
    )

    return {"response": response.choices[0].message.content.strip()}
