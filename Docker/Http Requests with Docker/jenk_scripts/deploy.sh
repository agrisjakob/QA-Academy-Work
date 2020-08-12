#!/bin/bash

sudo docker-compose build

sudo docker-compose push

sudo docker service update --image agrisjakob/app2:latest h_app2

sudo docker service update --image agrisjakob/app1:latest h_app1
