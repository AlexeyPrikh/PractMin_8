FROM python:3-alpine

MAINTAINER Alexey Prikhodko

COPY . /app

WORKDIR /app

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

CMD [ "python", "./app.py" ]