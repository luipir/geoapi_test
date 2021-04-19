# geoapi_test
Simple RESTFul geoapi guided by OpenAPI yaml definition

## How to install

    git clone https://github.com/luipir/geoapi_test.git

## How to run the server

    $> cd geoapi_test/python-flask-server
    $> docker-compose up

## API documention

Can be found at: API documented in: https://app.swaggerhub.com/apis/luipir/geo_test/1.0.0#/


## How to run integration tests

requirements: Need **libgeos** installed due to Shapely.

    $> cd geoapi_test/python-flask-server
    $> virtualenv -p `which python3` openapi_venv
    $> source ./openapi_venv/bin/activate
    (openapi_venv) $> pip3 install -r requirements.txt
    (openapi_venv) $> pip3 install -r test-requirements.txt
    (openapi_venv) $> pip3 install tox
    (openapi_venv) $> tox

## How to run unit tests

    $> cd geoapi_test/python-flask-server
    $> virtualenv -p `which python3` openapi_venv
    $> source ./openapi_venv/bin/activate
    (openapi_venv) $> pip3 install -r requirements.txt
    (openapi_venv) $> pip3 install -r test-requirements.txt
    (openapi_venv) $> pip3 install tox
    (openapi_venv) $> tox


## How I developed it

I decided to create the scheleton of all api and relative empty tests using **openapi-generator** basing on api specification in a swagger.yml:
https://github.com/luipir/geoapi_test/blob/develop/swagger.yaml

### difficulties
Because some limitations of the code generator (or my ignorance) I loosed a lot of time putting it at work.This reduced a lot the time to complete most of the test so I focused mainly in integration test to be sure to have a working server.
