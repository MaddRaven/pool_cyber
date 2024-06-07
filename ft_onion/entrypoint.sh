#!/bin/bash

/usr/sbin/tor -f /etc/tor/torrc
sleep 5
/usr/sbin/sshd -D -e -p 4343
nginx -g 'daemon off;'
tail -f /dev/null