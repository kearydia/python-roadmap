from fastapi import FastAPI

app = FastAPI()

@app.post("/chat")
def chat():
    return {"answer":"你的问题已经收到"}
