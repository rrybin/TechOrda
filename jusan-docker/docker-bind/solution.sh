wget https://github.com/rrybin/TechOrda/blob/main/docker/docker-bind/nginx.conf
sudo docker run -d -p 7777:80 --name jusan-docker-bind --mount type=bind,source="$(pwd)"/nginx/nginx.conf,target=/etc/nginx/nginx.conf  nginx:mainline
sudo docker ps
sudo docker inspect jusan-docker-bind
sudo docker logs jusan-docker-bind
