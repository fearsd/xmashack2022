FROM python:3.8-slim

WORKDIR /
COPY *.txt .

RUN pip install -r requirements.txt --no-cache-dir

# Install application
RUN mkdir /app
WORKDIR /app/
COPY src/*.py /app/

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "main:app", "--reload", "--timeout", "600"]

EXPOSE 8000