
# PoC Consul_BCN (registrator)

@date 2019-09-27
@version 1.0

## Description

This project is meant to show how to start a consul cluster and add automaticaly any docker container started in the hosts with the agent running.

**Flask app**

In the **flask** folder you can find a simple flask application: tt counts every visit to the flask (indibilually and in group).
It has a [Nginx](https://www.nginx.com/) load-balancer in front of our 3 flask instances. Those flask images save every visit in a redis database.

**Consul**

In the consul folder you can find the configuration to run **3 consul agents**,** 2 servers**, a **server bootstrap** and a **registrator**.

### Env vars needed

To run the **Flask** app, you need to specify the **nginx** version:
```
export NGINX_VERSION=latest
```
## Starting consul
```
cd consul
docker-compose --compatibility -f docker-compose-consul-cluster.yml up -d --force-recreate
```

## Starting Flask apps
```
cd flask
docker-compose up -d --force-recreate
```