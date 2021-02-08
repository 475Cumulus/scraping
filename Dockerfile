FROM python:3.8

# update pip
RUN pip install --upgrade pip

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY ./requirements.txt /usr/src

RUN pip install -r requirements.txt


