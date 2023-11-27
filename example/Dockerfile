FROM python:3.11.6 AS builder

ENV PYTHONUNBUFFERED 1


RUN pip install codefermenter
COPY . /src/
WORKDIR /src
RUN python -m codefermenter --remove-source direct --direct-files /src/main.py



FROM python:3.11.6-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app


COPY --from=builder /src /app

RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app --reload"] 