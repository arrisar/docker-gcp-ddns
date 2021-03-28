FROM gcr.io/google.com/cloudsdktool/cloud-sdk

LABEL maintainer="james@arrisar.com.au"

RUN \
  apt-get update && \
  apt-get install -y \
    cron \
    && \
  apt-get autoremove && \
  apt-get clean

RUN \
  pip3 install \
    pyyaml \
    requests

RUN mkdir -p /app/data

COPY ./app/* /app/

RUN set -e

ENTRYPOINT python3 /app/main.py