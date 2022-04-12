# init a base image (Alpine is small Linux distro)
FROM python:3.10.2-alpine3.15
# define the present working directory
WORKDIR /usr/app
# copy the contents into the working dir
ADD . /usr/app
# install some dependencies to install cryptography python module
# run pip to install the dependecies of the flask app
RUN apk add 
RUN apk add gcc \
        --no-cache \
        libressl-dev \
        musl-dev \
        libffi-dev && \
        pip install --upgrade pip && \
        pip install --upgrade setuptools && \
        pip install -r requirements.txt
# define the command to start the container
CMD ["python", "application.py"]
# gunicorn -w 2 -b 0.0.0.0:5000 preditivo:app