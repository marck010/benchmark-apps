
sudo docker build -t my-app-node .
sudo docker stop my-app-node   
sudo docker rm my-app-node
sudo docker run -m 200m --name my-app-node -d my-app-node
