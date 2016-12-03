FROM golang

MAINTAINER Konstantin Malanchev <hombit@gmail.com>

RUN go get github.com/prasmussen/gdrive

COPY ./docker-entrypoint.sh ./

ENTRYPOINT ["./docker-entrypoint.sh"]
