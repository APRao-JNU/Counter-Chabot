from transformers import pipeline
moderation_model = pipeline("text-classification", model="unitary/toxic-bert")
sentiment_model = pipeline("sentiment-analysis")
def moderate(text): 
    results = moderation_model(text)
    if any(r["label"].lower() in ["toxic", "offensive", "hate"] for r in results): 
        return "I prefer not to respond in an offensive manner."
    return text
def detect_sentiment(text): 
    result = sentiment_model(text)[0]
    return result["label"]
