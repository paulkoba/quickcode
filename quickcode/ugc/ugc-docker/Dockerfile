FROM alpine:latest

VOLUME "/project"
WORKDIR "/project"

RUN apk update && \
    apk upgrade && \
    apk --update add \
        gcc \
        g++ \
        build-base \
        bash \
        libstdc++ && \
    rm -rf /var/cache/apk/*

RUN PATH="/project:$PATH"

ENTRYPOINT [ "bash", "-c" ]