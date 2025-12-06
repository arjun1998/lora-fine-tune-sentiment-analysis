# Sentiment API

A FastAPI service for sentiment classification using a fine-tuned DistilBERT model hosted on Hugging Face Hub.

## ?? Run locally

```bash
docker build -t sentiment-api .
docker run -d -p 8000:8000 sentiment-api '''
