FROM python:3.9.20
WORKDIR /app
EXPOSE 8080
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install "fastapi[standard]"
COPY ./main.py /app
CMD ["fastapi", "run", "/app/main.py", "--port", "8080"]
