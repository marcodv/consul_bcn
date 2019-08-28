# PoC Consul_BCN

@date 2019-09-27
@version 1.0

## 1. Generate the app artifact for the app 'shopcart'

```bash
$ cd app
$ mvn clean package
```

## 2. Generate container instances for the app 'shopcart' + Consul agent (client)

```bash
$ cd docker
// Instance 1

--- TEMPORAL ---

$ docker-compose -f docker-compose-app.yml build --build-arg APP_PORT=8071
$ docker-compose -f docker-compose-app.yml up -d


CONTAINER_NAME=app-consul-1 APP_PORT=8071 docker-compose -f docker-compose-app.yml up -d
CONTAINER_NAME=app-consul-2 APP_PORT=8072 docker-compose -f docker-compose-app.yml up -d



```




--- TEMPORAL ---

```bash
$ docker-compose -f docker-compose-app.yml down --rmi all
```
