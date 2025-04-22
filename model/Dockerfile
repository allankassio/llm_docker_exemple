FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir transformers torch fastapi uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
