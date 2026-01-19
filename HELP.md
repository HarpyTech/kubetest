 ## 🚀 Purpose  
This repository demonstrates how to deploy a password‑protected **Redis** instance in a local Kubernetes cluster (via Docker Desktop) and validate the connection using a simple **Python client**.

---

## 📦 Prerequisites
- Docker Desktop with **Kubernetes enabled**  
- `kubectl` CLI configured to the `docker-desktop` context  
- Docker Hub account (optional, if you want to push images)  
- Python knowledge not required—everything runs inside Kubernetes

---

## 🔑 Step 1: Create Redis Password Secret
```bash
kubectl create secret generic redis-secret \
  --from-literal=redis-password=MyStrongP@ssw0rd
```

This stores the Redis password securely in Kubernetes.

---

## 🛠 Step 2: Deploy Redis
Apply the Redis Deployment and Service manifest:

```bash
kubectl apply -f redis-deployment.yaml
```

Verify:
```bash
kubectl get pods -l app=redis
kubectl get svc redis-service
```

---

## 🐍 Step 3: Build the Python Test Image
The repo includes `app.py` and `Dockerfile`.

Build locally:
```bash
docker build -t <your-dockerhub-username>/redis-test:1.0 .
```

(Optional) Push to Docker Hub:
```bash
docker push <your-dockerhub-username>/redis-test:1.0
```

---

## 🧪 Step 4: Run Validation Job
Apply the Kubernetes Job manifest:

```bash
kubectl apply -f redis-validate-job.yaml
```

Check logs:
```bash
kubectl logs job/redis-validate
```

Expected output:
```
Redis connection successful (attempt 1), value: Hello Redis!
```

---

## 🔄 Step 5: (Optional) Run as Deployment
If you want a long‑running pod for repeated checks:

```bash
kubectl apply -f redis-test-deployment.yaml
kubectl logs -l app=redis-test --follow
```

---

## 🛡 Troubleshooting
- **Secret missing** → `kubectl get secret redis-secret`  
- **Pod not running** → `kubectl describe pod <pod-name>`  
- **Connection refused** → Ensure `redis-service` exists and Redis pod is healthy  
- **Image pull error** → Push your image to Docker Hub or use `imagePullPolicy: Never` for local builds  

---
