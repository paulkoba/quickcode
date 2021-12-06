FROM python:3.7-alpine

VOLUME "/project"
WORKDIR "/project"

RUN apk update && \
    apk upgrade && \
    apk --update add bash


RUN PATH="/project:$PATH"

ENTRYPOINT [ "bash", "-c" ]