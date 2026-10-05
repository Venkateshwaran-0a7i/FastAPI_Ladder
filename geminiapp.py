# from google import genai
# from datetime import datetime
import uvicorn

# client = genai.Client(api_key="AQ.Ab8RN6LbG9CZQcANjtpFu_6C6VwO7ZBOXhv7Z_y3NFZ0wQoKdg")

from fastapi import FastAPI
from google import genai
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@app.get("/")
def home():
    return {"message": "Gemini chatbot is running"}


@app.get("/chat")
def chat(message: str):

    current_datetime = datetime.now()

    prompt = f"""
    Current date and time: {current_datetime}

    User question:
    {message}

    Answer the user. If they ask about the current date or time,
    use the provided current date and time.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "user": message,
        "gemini": response.text
    }

if __name__ == "__main__":
    uvicorn.run("geminiapp:app", host="0.0.0.0", port=8000, reload=True)