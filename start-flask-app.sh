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

# Start the Flask app using Gunicorn on port 8000 (Nginx will reverse proxy HTTPS to this)
/home/ec2-user/Christmas_Eve_Eve_Calculator/venv/bin/gunicorn \
  application:application \
  -w 1 -b 127.0.0.1:8000
