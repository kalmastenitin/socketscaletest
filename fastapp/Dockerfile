FROM tiangolo/uvicorn-gunicorn:python3.11-slim

RUN apt-get update && apt-get install -y netcat

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .