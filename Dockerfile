FROM ubuntu:22.04

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y \
    cmake \
    python3.10 \
    python3-distutils \
    python3-dev

WORKDIR /app

COPY cpp/ cpp
COPY python/ python

CMD ["/bin/bash", "./bootstrap.sh"]
