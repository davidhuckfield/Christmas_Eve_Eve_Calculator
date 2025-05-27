#!/bin/bash
source /home/ec2-user/Christmas_Eve_Eve_Calculator/venv/bin/activate
cd /home/ec2-user/Christmas_Eve_Eve_Calculator/
pkill gunicorn || true
gunicorn --certfile=/etc/letsencrypt/live/xmas-eve-eve.com/fullchain.pem \
         --keyfile=/etc/letsencrypt/live/xmas-eve-eve.com/privkey.pem \
         -w 1 -b 0.0.0.0:443 application:application