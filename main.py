from fastapi import FastAPI
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Model + tokenizer setup
# Use DistilBERT tokenizer (base) and load your fine-tuned model weights
model_name = "ArjunWK/distilbert-base-uncased-lora-text-classification"
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Input schema
class InputText(BaseModel):
    text: str

# Label mapping
labels = {0: "negative", 1: "positive"}

@app.post("/predict")
def predict(input: InputText):
    # Tokenize input
    inputs = tokenizer(input.text, return_tensors="pt")
    outputs = model(**inputs)

    # Get probabilities
    probs = torch.softmax(outputs.logits, dim=1)

    # Predicted class
    pred_class = torch.argmax(probs, dim=1).item()
    confidence = probs[0][pred_class].item()

    return {
        "prediction": labels[pred_class],
        "confidence": round(confidence, 4)
    }

# Optional root endpoint
@app.get("/")
def root():
    return {"message": "Sentiment API is running!"}
