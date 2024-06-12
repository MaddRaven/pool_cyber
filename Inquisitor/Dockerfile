FROM ubuntu:latest

WORKDIR /inquisitor

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev libpcap-dev libnet-dev python3-venv -y

RUN apt -y install libpcap0.8

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install scapy argparse getmac libpcap

COPY inquisitor .
RUN chmod 777 inquisitor

CMD /bin/bash -c "tail -f /dev/null"
