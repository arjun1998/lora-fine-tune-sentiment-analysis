FROM python:3.10-slim

WORKDIR /app

# Install core dependencies in small chunks
RUN pip install --no-cache-dir fastapi uvicorn[standard]
RUN pip install --no-cache-dir transformers protobuf
RUN pip install --no-cache-dir peft

# Install Torch CPU-only from PyTorch index
RUN pip install --no-cache-dir torch==2.1.0 --index-url https://download.pytorch.org/whl/cpu

# Copy app code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

