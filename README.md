AI DevOps Project: ML Model Deployment with FastAPI & Docker

Overview

This project demonstrates a simple end-to-end DevOps pipeline for AI deployment.
A machine learning model is trained and deployed as a REST API using FastAPI, containerized with Docker, and integrated with CI/CD using GitHub Actions.

Project Features
Train and save ML model (Iris dataset)
Build API using FastAPI
Test API using Swagger UI
Containerize application using Docker
CI/CD pipeline using GitHub Actions

Tech Stack
Python
Scikit-learn
FastAPI
Uvicorn
Docker
GitHub Actions
 Project Structure
ai-devops-project/
│
├── app.py              # FastAPI application
├── model.pkl           # Trained ML model
├── requirements.txt    # Dependencies
├── Dockerfile          # Docker configuration
└── .github/workflows/
    └── ci.yml          # CI/CD pipeline

Learning Outcomes
Understanding of MLOps basics
Model deployment using FastAPI
Containerization using Docker
Automation using CI/CD pipelines

Future Improvements
Add model monitoring (Prometheus + Grafana)
Deploy on cloud (AWS / Render)
Add frontend UI

Authors

Saksham Chopra, Yashika Tomar, Aditi Verma
