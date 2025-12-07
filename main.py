from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from peft import PeftModel
import torch
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Base model + tokenizer
base_model_name = "distilbert-base-uncased"
adapter_repo = "ArjunWK/distilbert-base-uncased-lora-text-classification"

tokenizer = AutoTokenizer.from_pretrained(base_model_name)
base_model = AutoModelForSequenceClassification.from_pretrained(base_model_name)
model = PeftModel.from_pretrained(base_model, adapter_repo)

# Input schema
class InputText(BaseModel):
    text: str

# Label mapping
labels = {0: "negative", 1: "positive"}

@app.get("/")
def health_check():
    return {"status": "ok", "message": "FastAPI app is running!"}

@app.post("/predict")
def predict(input: InputText):
    # Tokenize input
    inputs = tokenizer(input.text, return_tensors="pt", truncation=True, padding=True)
    # Run through model
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=-1).item()
    return {"label": labels[prediction], "score": torch.softmax(outputs.logits, dim=-1).tolist()}

# Run Uvicorn when executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
