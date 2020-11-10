From python:stretch

copy . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install requirements.txt
ENTRYPOINT ["gunicorn","-b",":8080","main:APP"]