#!/bin/sh
docker-compose --compatibility -f docker-compose-consul-cluster.yml up -d --force-recreate
