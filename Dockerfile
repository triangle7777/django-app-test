FROM python:3.7-alpine
MAINTAINER Jason Lebreton

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements /requirements
RUN pip install -r /requirements

RUN mkdir /app
WORKDIR /app
COPY . .

RUN adduser -D user
USER user
