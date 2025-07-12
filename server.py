import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from app.twiml import router as twiml_router
from app.stream import router as stream_router

app = FastAPI()
app.include_router(twiml_router)
app.include_router(stream_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
