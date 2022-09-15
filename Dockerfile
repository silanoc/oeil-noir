FROM python:3.9-slim

LABEL version="1.0" maintainer="silanoc https://github.com/silanoc"

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt && rm requirements.txt

ADD . /app/

EXPOSE 80

ENTRYPOINT ["python", "main.py"]