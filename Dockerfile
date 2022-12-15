FROM python:3.8-slim

# Install basic requirements for application
RUN apt-get update && \
    apt-get install -y gcc antiword unrtf poppler-utils tesseract-ocr wget \
    && rm -rf /var/lib/apt/lists/* \
    && apt clean


# install languages
WORKDIR /usr/share/tesseract-ocr/4.00/tessdata/
COPY install-languages.sh .
RUN chmod +x ./install-languages.sh
RUN ./install-languages.sh

RUN tesseract --list-langs


WORKDIR /
COPY *.txt .

RUN pip install -r requirements.txt --no-cache-dir 
RUN pip uninstall -y -r requirements_delete.txt


# Install applicaiton

RUN mkdir /app
WORKDIR /app/
COPY src/*.py /app/
RUN mkdir /files
WORKDIR /files/
COPY files/*.pdf /files/
WORKDIR /app/

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "main:app", "--reload", "--timeout", "600"]

EXPOSE 8000