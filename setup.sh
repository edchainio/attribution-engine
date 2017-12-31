#!/usr/bin/env bash

apt-get -y install python3-pip virtualenv
git clone git://github.com/edchainio/attribution_engine.git
cd attribution_engine
virtualenv --no-site-packages venv
source venv/bin/activate
pip3 install -r requirements.txt
