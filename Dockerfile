FROM python:3.10-slim

WORKDIR /app

# Install system dependencies needed for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip first
RUN pip install --upgrade pip

# Install Python dependencies in smaller chunks
RUN pip install --no-cache-dir fastapi==0.110.0 uvicorn[standard]==0.29.0
RUN pip install --no-cache-dir transformers==4.37.2 peft==0.7.1
RUN pip install --no-cache-dir torch==2.1.2 --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir huggingface-hub==0.20.3 pydantic==2.6.4 numpy<2 protobuf

# Copy app code
COPY . .

EXPOSE 10000

CMD ["python", "main.py"]
