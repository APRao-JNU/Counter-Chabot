from fastapi import FastAPI
from pydantic import BaseModel
from intent_model import classify_intent
from generation import generate_counter
from moderation import moderate
from db import retrieve_similar

app = FastAPI()

class SocialPost(BaseModel): text: str

@app.post("/counter-reply")
async def counter_reply(request: SocialPost):
    intent = classify_intent(request.text)
    retrieved = retrieve_similar(request.text)
    reply = generate_counter(request.text, intent, retrieved)
    final_reply = moderate(reply)
    return {"reply": final_reply, "intent": intent}
if __name__ == "__main__":
    import uvicorn
    print("✅ CounterBot API is running on port 8000")
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
