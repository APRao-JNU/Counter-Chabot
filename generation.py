from transformers import pipeline
from prompts import BASE_PROMPT
generator = pipeline("text-generation", model="gpt2")
def generate_counter(text, intent, retrieved): 
    prompt = BASE_PROMPT.format(post=text, ideology=intent["ideology"], examples=retrieved or "")
    result = generator(prompt, max_length=100, do_sample=True, temperature=0.7)
    return result[0]["generated_text"].split("Response:")[-1].strip()
