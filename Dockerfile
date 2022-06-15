FROM python:3.8-buster 

WORKDIR /app

COPY . .
RUN pip install --upgrade pip

RUN pip install -r requirements.txt 

ARG FLASK_APP=app.py

ENTRYPOINT [ "python3", "app.py"]