#!/bin/env bash
docker run --rm -u "$(id -u):$(id -g)" -v ${PWD}:/local -v${PWD}/../../python-flask-server/:/out   openapitools/openapi-generator:cli-v5.1.0 generate -i /local/swagger.yaml -g python-flask -o /out
if [ $? -eq 1 ]; then
	exit
fi
pushd .
cd ../../python-flask-server
docker build -t swagger_server:latest .
pushd
docker rm --force swagger_server
docker run --name swagger_server -p 8080:8080 swagger_server 
