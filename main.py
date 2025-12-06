from fastapi import FastAPI
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from pydantic import BaseModel
app = FastAPI()

model_name = "ArjunWK/distilbert-base-uncased-lora-text-classification"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


# Define input schema
class InputText(BaseModel):
    text: str

# Label mapping
labels = {0: "negative", 1: "positive"}

@app.post("/predict")
def predict(text: str):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    # Get probabilities
    probs = torch.softmax(outputs.logits, dim=1)

    # Get predicted class
    pred_class = torch.argmax(probs, dim=1).item()
    confidence = probs[0][pred_class].item()
    
    return {
        "prediction": labels[pred_class],
        "confidence": round(confidence, 4)  # e.g. 0.9231
    }
