FROM python:3.4-slim

RUN apt-get -y update
RUN apt-get -y install nano

# MongoDB 
ENV mongo_host mongo
ENV mongo_port 27017

ADD syslog-server /application
WORKDIR /application

RUN python setup.py develop

CMD ["nginx-to-mongodb"]