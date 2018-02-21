#!/bin/bash

sudo docker build -t my-app-netcore .
sudo docker stop my-app-netcore   
sudo docker rm my-app-netcore
sudo docker run -m 200m --name my-app-netcore -v `pwd`/opt/my-app-netcore  -d my-app-netcore
