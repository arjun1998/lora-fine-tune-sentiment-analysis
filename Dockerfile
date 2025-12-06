FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Install all packages from PyPI
RUN pip install --no-cache-dir -r requirements.txt

# Reinstall torch from CPU-only index (overrides CUDA build)
RUN pip install --no-cache-dir torch==2.1.0+cpu --index-url https://download.pytorch.org/whl/cpu

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
