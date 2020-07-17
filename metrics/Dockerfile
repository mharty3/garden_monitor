FROM python:3.7-alpine
RUN apk update && apk add build-base

WORKDIR /app

RUN pip install Adafruit_DHT Flask
EXPOSE 5000

COPY . .

CMD python sensor.py
