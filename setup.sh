#!/usr/bin/env bash

apt-get -y install python3-pip virtualenv
virtualenv -p python3 --no-site-packages venv
source venv/bin/activate
pip3 install -r requirements.txt
