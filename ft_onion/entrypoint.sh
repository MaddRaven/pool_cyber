#!/bin/bash

echo "Starting Tor..."
/usr/sbin/tor -f /etc/tor/torrc
sleep 5

echo "Starting SSHD..."
/usr/sbin/sshd -D -e -p 4343

echo "Starting Nginx..."
nginx -g 'daemon off;'

echo "Container ready."
tail -f /dev/null