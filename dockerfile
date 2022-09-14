FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt && rm requirements.txt

COPY domaine/ /app/domaine
COPY interface/console/ /app/interface/console
COPY interface/json /app/interface/json
COPY images/ /app/images
COPY main.py /app

EXPOSE 80

ENTRYPOINT ["python", "main.py"]