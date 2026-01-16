FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/lists/*

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir "jaraco.context>=6.1.0"

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/logs

COPY app/ .

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \

CMD curl --fail http://localhost:8080/health || exit 1 

CMD ["python", "main.py"] 
