FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install --no-cache-dir redis==5.0.1
CMD ["python", "app.py"]
