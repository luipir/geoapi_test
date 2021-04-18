#!/bin/env bash
pushd .
cd python-flask-server
docker build -t swagger_server:latest .
pushd
docker rm --force swagger_server
docker run -d -u "$(id -u):$(id -g)" -v ${PWD}/python-flask-server/openapi_server:/usr/src/app/openapi_server --name swagger_server -p 8080:8080 swagger_server 
tail -f ${PWD}/python-flask-server/openapi_server/log.txt
