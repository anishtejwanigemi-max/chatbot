from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import traceback
from nomic import embed
from fastapi.responses import StreamingResponse
import json

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class CodeRequest(BaseModel):
    code: str

# Response model (only explanation now)
class ExplanationResponse(BaseModel):
    explanation: str

# Environment configuration
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama2")

@app.post("/explain")
def explain_code(req: CodeRequest):
    code = req.code.strip()
    if not code:
        raise HTTPException(status_code=400, detail="Code snippet is required.")

    # Optional: Validate that the embed works (but we ignore the result)
    try:
        _ = embed.text([code])  # Just to verify it doesn't fail
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Embedding error: {str(e)}")

    prompt = (
        "Explain what the following code does as if you were talking to a five-year-old. "
        "Be very simple and clear.\n\nCode:\n" + code
    )
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": True  # Enable streaming
    }

    def stream_ollama():
        with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if line:
                    try:
                        data = json.loads(line)
                        chunk = data.get("response") or data.get("text")
                        if chunk:
                            yield chunk
                    except Exception:
                        continue

    return StreamingResponse(stream_ollama(), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

