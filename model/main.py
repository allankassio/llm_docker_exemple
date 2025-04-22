from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI()
generator = pipeline("text-generation", model="gpt2")

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return {"result": result[0]['generated_text']}
