FROM python:3.7
WORKDIR /django_push_server/

COPY requirements.txt /django_push_server/
RUN pip install -r requirements.txt

COPY . /django_push_server/
