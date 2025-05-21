#!/bin/bash
cd /home/ec2-user/Christmas_Eve_Eve_Calculator
source venv/bin/activate
exec gunicorn -b 0.0.0.0:5000 application:application