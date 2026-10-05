from typing import Any, Dict

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI(title="AI + FastAPI Project")


class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 200


@app.post("/generate")
async def generate_text(request: PromptRequest) -> Dict[str, Any]:
    # Replace with real OpenAI SDK call in production.
    reply = f"This is a sample AI response for: {request.prompt}"
    return {
        "prompt": request.prompt,
        "response": reply,
        "tokens_used": request.max_tokens,
    }


@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)) -> dict:
    if not file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Image received. Process with OCR or AI in the next step.",
    }


@app.get("/stream")
async def stream_response() -> StreamingResponse:
    async def stream() -> Any:
        for chunk in ["Hello", ", ", "AI", " world", "!\n"]:
            yield chunk

    return StreamingResponse(stream(), media_type="text/plain")


# Production notes:
# - Use the OpenAI Python SDK for chat completions and image analysis.
# - Use BackgroundTasks or Celery for long operations.
# - Store uploaded files and pass them to OCR or AI pipelines.
