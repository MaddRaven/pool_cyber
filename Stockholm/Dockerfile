FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

ENV VIRTUAL_ENV=/var/www/html/myapp
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN $VIRTUAL_ENV/bin/pip install argparse cryptography

RUN mkdir -p /root/infection
COPY stockholm .
COPY Makefile-stockholm ./Makefile
COPY example_files/* /root/infection
COPY wannacry_ext.txt .
RUN chmod 777 stockholm

CMD /bin/bash -c "tail -f /dev/null"