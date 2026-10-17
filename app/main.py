import os
import uvicorn
from dotenv import load_dotenv

from fastapi import FastAPI

load_dotenv()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from infra-daily!"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
