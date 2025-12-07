
# Sentiment Analysis with DistilBERT + PEFT (LoRA) 🚀

## Overview
This project demonstrates how to fine‑tune **DistilBERT** for sentiment classification and then apply **Parameter‑Efficient Fine‑Tuning (PEFT)** with **LoRA adapters** to achieve strong performance while keeping training lightweight and scalable.

Beyond experimentation, the project shows how to **deploy the model in production** using:
- **FastAPI** for serving predictions via REST API
- **Docker** for containerization and reproducibility
- **AWS EC2** for hosting the service in the cloud

---

## ✨ Key Highlights
- Compared **base model fine‑tuning** vs. **LoRA adapter training**
- Showcased how **PEFT reduces compute cost** while maintaining accuracy
- Built a reproducible workflow for sentiment analysis with Hugging Face + PEFT
- Wrapped the model in a **FastAPI app**, containerized with **Docker**, and deployed on **EC2**

---
## Quick Road Map of the Project

```mermaid
flowchart TD
    A[Load DistilBERT Base Model] --> B[Fine‑Tune for Sentiment Classification]
    B --> C[Apply PEFT - LoRA Adapters]
    C --> D[Save Adapter + Config]
    D --> E[FastAPI Service for Inference]
    E --> F[Docker Containerization]
    F --> G[Deploy on AWS EC2 Instance]
    G --> H[Public API Endpoint]

---

## 🛠️ Tech Stack
- **Model**: DistilBERT (Hugging Face Transformers)
- **Fine‑Tuning**: PEFT (LoRA adapters)
- **Serving**: FastAPI + Uvicorn
- **Containerization**: Docker
- **Deployment**: AWS EC2

---

## 📂 Project Structure
```
.
├── main.py              # FastAPI app entrypoint
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container build instructions
├── notebooks/           # Training & fine‑tuning experiments
└── README.md            # Project documentation
```

---

## ⚡ Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/sentiment-api.git
cd sentiment-api
```

### 2. Build Docker image
```bash
sudo docker build -t sentiment-api .
```

### 3. Run container
```bash
sudo docker run -it --rm -p 10000:10000 sentiment-api
```

### 4. Test API
```bash
curl -X POST http://localhost:10000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "I love this movie!"}'
```

---

## 🌐 Deployment on EC2
1. Launch an EC2 instance (Ubuntu recommended).
2. Install Docker:
   ```bash
   sudo apt update && sudo apt install docker.io -y
   ```
3. Pull your repo and build:
   ```bash
   git pull origin main
   sudo docker build -t sentiment-api .
   sudo docker run -it --rm -p 10000:10000 sentiment-api
   ```
4. Open port **10000** in your EC2 security group.
5. Access your API at:
   ```
   http://<your-ec2-public-ip>:10000/
   ```

---

## 🔒 Optional: Nginx Reverse Proxy + HTTPS
For production, you can serve the API on port 80/443 with Nginx and secure it using Let’s Encrypt.

---

## 📊 Example Response
```json
{
  "label": "POSITIVE",
  "score": 0.987
}
```

---

## 📚 References
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [PEFT Library](https://huggingface.co/docs/peft)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://docs.docker.com/)
- [AWS EC2](https://docs.aws.amazon.com/ec2/)

---

## 🚀 Future Work
- Add CI/CD pipeline for automated deployment
- Extend to multi‑class sentiment datasets
- Benchmark inference latency under load

---

## 👨‍💻 Author
Built with ❤️ by arjun1998

```

---




