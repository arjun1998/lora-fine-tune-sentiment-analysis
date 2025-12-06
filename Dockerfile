FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Install FastAPI, Uvicorn, Transformers from PyPI
RUN pip install --no-cache-dir fastapi uvicorn[standard] transformers

# Install Torch CPU-only
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
