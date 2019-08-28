# PoC Consul_BCN

@date 2019-09-27
@version 1.0

## Info

- https://learn.hashicorp.com/consul/getting-started/services

## 1. Generate the app docker image for the app 'shopcart'

```bash
$ cd app
$ mvn clean package
$ docker build -t poc-consul/app -f docker/Dockerfile .
```

## 2. Generate and manage containers instances for the app 'shopcart'

### 2.1. Start container instances for the app

```bash
$ cd docker
$ docker-compose --compatibility -f docker-compose-apps.yml up -d --force-recreate
```

### 2.2. Check instances for the app

```bash
$ curl -X GET http://localhost:8071/health
$ curl -X GET http://localhost:8072/health
$ curl -X GET http://localhost:8073/health
```

Check API with SwaggerUI: 

- http://localhost:8071/swagger-ui.html
- http://localhost:8072/swagger-ui.html
- http://localhost:8073/swagger-ui.html

### 2.3. Stop container instances for the app

```bash
$ cd docker
$ docker-compose -f docker-compose-apps.yml down
```

## 3. Generate and manage containers instances for the Consul cluster

### 3.1. Start container instances for the cluster

```bash
$ cd docker
$ docker-compose --compatibility -f docker-compose-consul-cluster.yml up -d --force-recreate
```

### 3.2. Check Consul cluster

- http://localhost:8500/

### 3.3. Stop container instances for the cluster

```bash
$ cd docker
$ docker-compose -f docker-compose-consul-cluster.yml down
``` 


TODO:

- Register services of the apps in consul: file in each docker container

    - https://learn.hashicorp.com/consul/getting-started/services

- Register services of the apps in consul: docker consul registrator

    - https://github.com/gliderlabs/registrator

- How to call the app APIs throught Consul
- PoC of all Consul configurations
