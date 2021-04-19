#!/bin/env bash
docker run --rm \
	-u "$(id -u):$(id -g)" \
	-v ${PWD}:/local \
	openapitools/openapi-generator:cli-v5.1.0 generate \
	-i /local/swagger.yaml \
	-g python \
	-o /local/python-flask-client/
if [ $? -eq 1 ]; then
	exit
fi