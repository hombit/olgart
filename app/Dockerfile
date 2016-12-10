FROM python:3.4

MAINTAINER Konstantin Malanchev <hombit@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN mkdir /olgart
WORKDIR /olgart

ADD requirements.txt /olgart/
RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y gettext

ADD . /olgart/
ADD ./static /www/static

CMD ["./docker-entrypoint.sh"]
