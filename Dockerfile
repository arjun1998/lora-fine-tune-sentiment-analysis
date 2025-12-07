FROM python:3.10-slim

WORKDIR /app

# Install system dependencies (optional but helps with builds)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

EXPOSE 10000

# Let main.py handle $PORT dynamically
CMD ["python", "main.py"]
