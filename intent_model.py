from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
LABELS = ["capitalism", "socialism", "conservatism", "liberalism", "other"]
def classify_intent(text): 
    result = classifier(text, candidate_labels=LABELS)
    return {"ideology": result["labels"][0], "scores": result["scores"]}
