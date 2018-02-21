
sudo docker build -t my-app-python .
sudo docker stop my-app-python   
sudo docker rm my-app-python
sudo docker run -m 200m --name my-app-python -d my-app-python
