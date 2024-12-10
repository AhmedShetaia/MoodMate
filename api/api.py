from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot import chat_response
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# FastAPI app
app = FastAPI()

# Request model
class ChatRequest(BaseModel):
    user_input: str

# Route for chatbot
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Get the API key from the environment
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="Google API key not found in environment variables.")

        response = chat_response(input_text=request.user_input, api_key=api_key)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
