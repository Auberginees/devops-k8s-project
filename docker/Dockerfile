FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/logs

COPY app/ .

EXPOSE 8080

CMD ["python", "main.py"] 

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \

CMD curl --fail http://localhost:8080/health || exit 1 

