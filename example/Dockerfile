FROM python:3.11.6 AS builder

ENV PYTHONUNBUFFERED 1


RUN pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple codefermenter==0.1.0
COPY ./src /src
WORKDIR /src
RUN python -m codefermenter --remove-source recursive --source-dir /src/


FROM python:3.11.6-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app


COPY --from=builder /src /app

RUN pip install -r requirements


CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000