
# Example Usage of the Codefermenter Obfuscator in Docker Container

This README outlines an example of using the Codefermenter obfuscator during Docker container build process. 
The purpose is to include an obfuscated file in the container instead of the original source code.

## Building Process

The build process is carried out in two stages:

### Stage 1: Installation and Obfuscation

In the first stage, we install the Codefermenter module and perform recursive obfuscation or transformation.

```Dockerfile
FROM python:3.11.6 AS builder

ENV PYTHONUNBUFFERED 1

RUN pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple codefermenter==0.1.0
COPY ./src /src
WORKDIR /src
RUN python -m codefermenter --remove-source recursive --source-dir /src/
```

### Stage 2: Preparing the Working Container

The second stage involves preparing the working container, installing dependencies, etc.

```Dockerfile
FROM python:3.11.6-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=builder /src /app

RUN pip install -r requirements.txt

CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

## Post-Build

After the build, a `main.cpython-311-x86_64-linux-gnu.so` file is generated, and the original `main.py` is removed, as the `--remove-source` flag is used.

Running `docker run -ti --rm example ls` should display the `main.cpython-311-x86_64-linux-gnu.so` module and `requirements.txt`.

## Running the Application

To launch Uvicorn, use:

```bash
docker run -ti -p 127.0.0.1:8000:8000 --rm example
```

You should see output similar to:

```
INFO:     Started server process [8]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

This README provides an example of using the Codefermenter obfuscator to ensure that the Docker container includes an obfuscated file instead of the original source code.
