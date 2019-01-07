FROM python:3.6-slim
RUN apt-get update
RUN apt-get install -y git
RUN mkdir -p /usr/src/app
ADD requirements.txt /usr/src/app/requirements.txt
ADD servant /usr/src/app/servant
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
