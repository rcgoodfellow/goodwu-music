FROM debian:latest

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install flask elasticsearch

WORKDIR /www

COPY . .

ENV FLASK_APP musicsite.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

CMD flask run -h 0.0.0.0 -p 80
