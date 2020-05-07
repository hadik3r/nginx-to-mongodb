# Storing Nginx logs in MongoDB

If you have trouble using Fluentd to store your Nginx logs into MongoDB, here is a simple alternative solution. It uses a container that works as a Syslog server to receive logs from Nginx. The logs are then converted to JSON format, and, finally, stored in MongoDB.

# Requirement

- Docker-compose needs to be installed on your machine

## Usage

Take the following steps to run the containers:

``` git clone https://github.com/hadik3r/nginx-to-mongodb.git && cd nginx-to-mongodb ```

``` docker-compose up -d ```
