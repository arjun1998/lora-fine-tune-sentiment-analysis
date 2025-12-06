from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from peft import PeftModel
import torch
from pydantic import BaseModel

app = FastAPI()

# Base model + tokenizer
base_model_name = "distilbert-base-uncased"
adapter_repo = "ArjunWK/distilbert-base-uncased-lora-text-classification"

tokenizer = AutoTokenizer.from_pretrained(base_model_name)
base_model = AutoModelForSequenceClassification.from_pretrained(base_model_name)

# Apply LoRA adapter
model = PeftModel.from_pretrained(base_model, adapter_repo)

# Input schema
class InputText(BaseModel):
    text: str

# Label mapping
labels = {0: "negative", 1: "positive"}

@app.post("/predict")
def predict(input: InputText):
    inputs = tokenizer(input.text, return_tensors="pt")
    outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=1)
    pred_class = torch.argmax(probs, dim=1).item()
    confidence = probs[0][pred_class].item()

    return {
        "prediction": labels[pred_class],
        "confidence": round(confidence, 4)
    }

@app.get("/")
def root():
    return {"message": "Sentiment API with LoRA adapter is running!"}
