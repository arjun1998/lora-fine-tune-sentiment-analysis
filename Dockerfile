FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    fastapi==0.110.0 \
    uvicorn[standard]==0.29.0 \
    transformers==4.36.2 \
    protobuf \
    peft \
    torch==2.1.2 --index-url https://download.pytorch.org/whl/cpu \
    huggingface-hub==0.20.3 \
    pydantic==2.6.4

COPY . .

EXPOSE 10000

CMD ["python", "main.py"]
