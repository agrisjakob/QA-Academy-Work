#!/bin/bash
sudo apt install python3-pip python3-venv

python3 -m venv venv
. ./venv/bin/activate

pip3 install flask flask-testing pytest pytest-cov requests Werkzeug==0.16.1

cd /home/jenkins/.jenkins/workspace/'Docker requests project'/app1
pytest --cov app1 --cov-report term-missing


cd /home/jenkins/.jenkins/workspace/'Docker requests project'/app2

pytest --cov app2 --cov-report term-missing
