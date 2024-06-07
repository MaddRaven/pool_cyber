FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y nginx openssh-server tor sudo && \
    mkdir -p /var/www/html /var/run/sshd /var/lib/tor/hidden_service/

RUN chown debian-tor:debian-tor /var/lib/tor/hidden_service/ && \
    chmod 700 /var/lib/tor/hidden_service/ && \
    chmod 644 /etc/tor/torrc

COPY nginx.conf /etc/nginx/
COPY --chown=nginx:nginx index.html /usr/share/nginx/html/
COPY sshd_config /etc/ssh/sshd_config
COPY torrc /etc/tor/torrc

EXPOSE 80 4343

USER debian-tor

CMD service tor start && service ssh start && service nginx start