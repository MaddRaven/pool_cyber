FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y nginx openssh-server tor sudo

RUN mkdir -p /var/www/html /var/run/sshd /var/lib/tor/hidden_service/

COPY nginx.conf /etc/nginx/
COPY --chown=nginx:nginx index.html /usr/share/nginx/html/
COPY sshd_config /etc/ssh/sshd_config
COPY torrc /etc/tor/torrc

RUN chown -R debian-tor:debian-tor /var/lib/tor /var/log/tor
RUN chmod 700 /var/lib/tor/hidden_service

EXPOSE 8080 4343

CMD /bin/bash -c "service tor start && service ssh start && service nginx start && tail -f /dev/null"