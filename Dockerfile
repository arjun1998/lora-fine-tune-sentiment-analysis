FROM python:3.10-slim

WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies (CPU-only torch)
RUN pip install --no-cache-dir -r requirements.txt \
    --index-url https://download.pytorch.org/whl/cpu

# Copy your app code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
