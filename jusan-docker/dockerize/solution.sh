sudo docker build -t jusan-fastapi-final:dockerized .
sudo docker run -d -p 8080:8080 --name jusan-dockerized jusan-fastapi-final:dockerized
