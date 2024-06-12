FROM ubuntu:latest

WORKDIR /inquisitor

RUN apt-get update && \
    apt-get install -y  python3-dev libpcap-dev libnet-dev -y

RUN pip3 install --upgrade pip
RUN pip3 install scapy
RUN pip3 install argparse
RUN pip3 install pcapy
RUN pip3 install getmac

COPY inquisitor .
COPY Makefile-inquisitor ./Makefile
RUN chmod 777 inquisitor

CMD /bin/bash -c "tail -f /dev/null"