# devops-k8s-project

## 📦 Project Overview

This repository contains a **DevOps / Kubernetes project** demonstrating core practices such as containerization, orchestration, infrastructure automation, and CI/CD.

The goal of this project is to showcase practical skills in working with **Docker**, **Kubernetes**, and related DevOps tools.

---

## 🛠️ Tech Stack

* **Docker** – application containerization
* **Kubernetes** – container orchestration
* **kubectl / Helm** – cluster and application management
* **CI/CD** – automated build and deployment (GitHub Actions / GitLab CI, if applicable)
* **Cloud / Local Cluster** – Minikube, Kind, or cloud provider

---
# 🚀 Infrastructure Health Check API

A lightweight HTTP service designed to demonstrate infrastructure monitoring, environment transparency, and Kubernetes integration.

## 📌 Object Overview
The **Infrastructure Health Check API** is a minimal service that provides essential data about its internal state and the environment it runs in. It is specifically built to showcase how applications interact with orchestrators like Kubernetes using Probes and Environment Variables.

### Key Features:
* **Service Vitality:** Instantly verify if the service is up and running.
* **Environment Transparency:** Displays versioning and environment-specific data (dev/stage/prod).
* **Kubernetes Ready:** Built-in endpoints for Liveness and Readiness probes.
* **Execution Context:** Provides startup time and system uptime info.

---

## 🛣 API Endpoints

| Endpoint | Method | Purpose | Description |
| :--- | :---: | :--- | :--- |
| `/` | `GET` | **Basic Check** | Returns a simple "Hello" to confirm connectivity. |
| `/health` | `GET` | **Liveness Probe** | Signals to Kubernetes that the container is alive. |
| `/ready` | `GET` | **Readiness Probe** | Signals that the app is ready to handle traffic. |
| `/version` | `GET` | **Version Info** | Displays the application version pulled from ENV. |
| `/env` | `GET` | **Env Context** | Shows current environment name (dev/prod/etc). |

---

## 🛠 Tech Stack
* **Language:** Python / Flask
* **Containerization:** Docker
* **Orchestration:** Kubernetes (K8s)
* **CI/CD:** GitHub Actions

---



## 📂 Repository Structure

```text
.
├── app/                # Application source code
├── docker/             # Dockerfiles and container configs
├── k8s/                # Kubernetes manifests (Deployments, Services, Ingress, etc.)
├── helm/               # Helm charts (if used)
├── scripts/            # Helper scripts
├── .github/workflows/  # CI/CD pipelines
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Docker
* Kubernetes cluster (Minikube / Kind / Cloud)
* kubectl
* Helm 

### Run Locally

```bash
# Build Docker image
docker build -t devops-k8s-project .

# Start local Kubernetes cluster
minikube start

# Deploy to Kubernetes
kubectl apply -f k8s/
```

Check running resources:

```bash
kubectl get pods
kubectl get services
```

---

## 🔄 CI/CD

This project includes a CI/CD pipeline that:

1. Builds Docker images
2. Runs basic checks/tests
3. Deploys the application to Kubernetes

Pipeline configuration can be found in:

```
.github/workflows/
```

---

## 📈 Key Features

* Containerized application
* Kubernetes deployment
* Scalable and reproducible infrastructure
* DevOps best practices

---

## 🧪 Testing

```bash
# Example
kubectl logs <pod-name>
```

---

## 📌 Future Improvements

* Add monitoring (Prometheus, Grafana)
* Add logging (ELK / Loki)
* Implement HPA
* Improve security (RBAC, NetworkPolicies)

---

## 👤 Author

**Denys Kokhan (Aen)**
DevOps / Cloud Engineer

---

## 📄 License

---
