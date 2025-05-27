#!/bin/bash
cd /home/ec2-user/Christmas_Eve_Eve_Calculator

# Activate virtual environment
source venv/bin/activate

# Pull latest changes
git pull origin main

# Install any new dependencies
pip install -r requirements.txt

# Kill any existing gunicorn process
pkill gunicorn || true

# Start the Flask app using Gunicorn with SSL
gunicorn -w 1 -b 0.0.0.0:443 application:application \
  --certfile=/etc/letsencrypt/live/xmas-eve-eve.com/fullchain1.pem \
  --keyfile=/etc/letsencrypt/live/xmas-eve-eve.com/privkey1.pem