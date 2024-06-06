FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y nginx openssh-server tor && \
    mkdir -p /var/www/html /var/run/sshd /var/lib/tor/hidden_service/

COPY nginx.conf /etc/nginx/sites-available/default
COPY index.html /var/www/html/
COPY sshd_config /etc/ssh/sshd_config

EXPOSE 80 4242

CMD ["/usr/sbin/tor", "-f", "/etc/tor/torrc"] & \
    /usr/sbin/sshd -D -e -p 4242