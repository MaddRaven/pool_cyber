FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv python-libpcap

ENV VIRTUAL_ENV=/var/www/html/myapp
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN $VIRTUAL_ENV/bin/pip install argparse

COPY inquisitor .
COPY Makefile-inquisitor ./Makefile
RUN chmod 777 inquisitor

CMD /bin/bash -c "tail -f /dev/null"