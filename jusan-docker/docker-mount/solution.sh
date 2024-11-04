curl -O https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf
curl -O https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip
sudo docker run -d -p 9999:80 --name jusan-docker-mount --mount type=bind,source="$(pwd)"/jusan-docker-mount.conf,target=/etc/nginx/conf.d/jusan-docker-mount.conf --mount type=bind,source="$(pwd)"/jusan-docker-mount,target=/var/www/example nginx:mainline
