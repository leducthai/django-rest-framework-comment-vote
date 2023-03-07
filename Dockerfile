# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /cm
COPY requirements.txt /cm/
RUN pip install -r requirements.txt
COPY . /cm/