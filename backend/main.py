from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transcript(BaseModel):
    text: str

@app.post("/transcribe/")
def save_transcript(data: Transcript):
    with open("transcripts.txt", "a", encoding="utf-8") as f:
        f.write(data.text + "\n")
    return {"status": "saved"}
