FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt update && apt install python3-dev build-essential libssl-dev -y

RUN pip install -r requirements.txt

RUN pip install -I --no-binary=:all: --no-cache-dir uwsgi==2.0.20

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# CMD gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 --bind 0.0.0.0:5000 run:app
CMD uwsgi --http :5000 --gevent 1000 --http-websockets --master --wsgi-file run.py --callable app