# coding: utf-8

from __future__ import absolute_import
import unittest
import logging
import sys
import json
from http import HTTPStatus

from flask import json
from six import BytesIO

import shapely

from openapi_server.models.area import Area  # noqa: E501
from openapi_server.models.point3_d_dict import Point3DDict  # noqa: E501
from openapi_server.test import BaseTestCase
from openapi_server.test.test_modification_controller import TestModificationController
from openapi_server.data.areas import getAreas, setAreas # noqa: E501

log = logging.getLogger(__name__)

class TestSearchController(BaseTestCase):
    """SearchController integration test stubs"""

    def setUp(self):
        # self.modController = TestModificationController()
        setAreas({})

    def _addAreas(self):
        area = {
            "date" : "2021-04-17",
            "name" : "Luigi Pirelli",
            "poly" : [ {
                "lat" : 0,
                "lon" : 0,
                "altitude" : 0
            }, {
                "lat" : 2,
                "lon" : 0,
                "altitude" : 1
            }, {
                "lat" : 2,
                "lon" : 2,
                "altitude" : 2
            }, {
                "lat" : 0,
                "lon" : 2,
                "altitude" : 3
            } ],
            "props" : {
                "key1" : "value1",
                "key2" : "value2"
            }
        }
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas',
            method='POST',
            headers=headers,
            data=json.dumps(area),
            content_type='application/json')
        self.assertStatus(response, HTTPStatus.NO_CONTENT, 'Response body is : ' + response.data.decode('utf-8'))

        area = {
            "date" : "2021-04-18",
            "name" : "Luigi Pipolo",
            "poly" : [ {
                "lat" : 1,
                "lon" : 1,
                "altitude" : 0
            }, {
                "lat" : 3,
                "lon" : 1,
                "altitude" : 1
            }, {
                "lat" : 3,
                "lon" : 3,
                "altitude" : 2
            }, {
                "lat" : 1,
                "lon" : 3,
                "altitude" : 3
            } ],
            "props" : {
                "key1" : "value3",
                "key2" : "value4"
            }
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas',
            method='POST',
            headers=headers,
            data=json.dumps(area),
            content_type='application/json')
        self.assertStatus(response, HTTPStatus.NO_CONTENT, 'Response body is : ' + response.data.decode('utf-8'))

    def test_get_area_by_date(self):
        """Test case for get_area_by_date

        Retrieve a Area with a specified data.
        """
        # check when date does not exist
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/date/{date}'.format(date='9999-12-31'),
            method='GET',
            headers=headers)
        self.assertStatus(response, HTTPStatus.NOT_FOUND, 'Response body is : ' + response.data.decode('utf-8'))

        # check when date exist

        # step1) add an entries
        # step2) check if I can get the entry via api
        
        # step 1
        self._addAreas()
        areas = getAreas()
        self.assertEqual(len(areas), 2)

        # step 2
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/date/{date}'.format(date='2021-04-18'),
            method='GET',
            headers=headers)
        self.assert200(response,'Response body is : ' + response.data.decode('utf-8'))

        result_areas = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(result_areas), 1)
        
        areas = getAreas()
        for area in result_areas:
            name = area['name']
            self.assertEqual(areas[name].to_dict(), area)

    def test_get_area_by_name(self):
        """Test case for get_area_by_name

        Retrieve a Area resource by unique name.
        """
        # check when name does not exist
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assertStatus(response, HTTPStatus.NOT_FOUND, 'Response body is : ' + response.data.decode('utf-8'))

        # check when name exist exist =>

        # step1) add an entries
        # step2) check if I can get the entry via api
        
        # step 1
        self._addAreas()
        areas = getAreas()
        self.assertEqual(len(areas), 2)

        # step 2
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/{name}'.format(name='Luigi Pirelli'),
            method='GET',
            headers=headers)
        self.assert200(response,'Response body is : ' + response.data.decode('utf-8'))

        # check when more than one key containing a search name =>
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/{name}'.format(name='Luigi'),
            method='GET',
            headers=headers)
        self.assert200(response,'Response body is : ' + response.data.decode('utf-8'))

        result_areas = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(result_areas), 2)
        
        areas = getAreas()
        for area in result_areas:
            name = area['name']
            self.assertEqual(areas[name].to_dict(), area)

    def test_get_area_by_properties(self):
        """Test case for get_area_by_properties

        Retrieve a Area with a specified data set of properties.
        """
        props = {
            "key1": "value1",
            "key2": "value2"
        }
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/properties',
            method='POST',
            headers=headers,
            data=json.dumps(props),
            content_type='application/json')
        self.assertStatus(response, HTTPStatus.NOT_FOUND, 'Response body is : ' + response.data.decode('utf-8'))

        # check when name exist exist =>

        # step1) add an entries
        # step2) check if I can get the entry via api
        # step3) check if nothing is found but something is stored
        
        # step 1
        self._addAreas()
        areas = getAreas()
        self.assertEqual(len(areas), 2)

        # step 2
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/properties',
            method='POST',
            headers=headers,
            data=json.dumps(props),
            content_type='application/json')
        self.assert200(response,'Response body is : ' + response.data.decode('utf-8'))

        result_areas = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(result_areas), 1)
        self.assertEqual(result_areas[0]['name'], 'Luigi Pirelli')

        # step 3
        props = {
            "key1": "value1111",
            "key2": "value2222"
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/properties',
            method='POST',
            headers=headers,
            data=json.dumps(props),
            content_type='application/json')
        self.assertStatus(response, HTTPStatus.NOT_FOUND, 'Response body is : ' + response.data.decode('utf-8'))

    def test_get_intersect(self):
        """Test case for get_intersect

        Retrieve a Area inteersecting posted polygon.
        """
        polygon = [ {
            "lat" : 1,   
            "lon" : 1,
            "altitude" : 1
            }, 
            {
                "lat" : 2,
                "lon" : 1,
                "altitude" : 2
            },
            {
                "lat" : 2,
                "lon" : 2,
                "altitude" : 3
            },
            {
                "lat" : 1,
                "lon" : 2,
                "altitude" : 4
            } 
        ]

        # first not found because no elements is stores
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/intersect',
            method='POST',
            headers=headers,
            data=json.dumps(polygon),
            content_type='application/json')
        self.assertStatus(response, HTTPStatus.NOT_FOUND, 'Response body is : ' + response.data.decode('utf-8'))

        # check when name exist exist =>

        # step1) add an entries
        # step2) check if I can get the entry via api
        # step3) check if nothing is found but something is stored
        self._addAreas()
        areas = getAreas()
        self.assertEqual(len(areas), 2)

        # step 2 - should get the two feature
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/intersect',
            method='POST',
            headers=headers,
            data=json.dumps(polygon),
            content_type='application/json')
        self.assert200(response,'Response body is : ' + response.data.decode('utf-8'))

        result_areas = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(result_areas), 2)
        self.assertEqual(result_areas[0]['name'], 'Luigi Pirelli')
        self.assertEqual(result_areas[1]['name'], 'Luigi Pipolo')

        # step 3: set a polygon that do not intersect
        polygon = [ {
            "lat" : 4,
            "lon" : 4,
            "altitude" : 1
            }, 
            {
                "lat" : 5,
                "lon" : 4,
                "altitude" : 2
            },
            {
                "lat" : 5,
                "lon" : 5,
                "altitude" : 3
            },
            {
                "lat" : 4,
                "lon" : 5,
                "altitude" : 4
            } 
        ]
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/intersect',
            method='POST',
            headers=headers,
            data=json.dumps(polygon),
            content_type='application/json')
        self.assertStatus(response, HTTPStatus.NOT_FOUND, 'Response body is : ' + response.data.decode('utf-8'))

    def test_get_intersection(self):
        """Test case for get_intersection

        Retrieve Area inside input polygon.
        """
        # equal to the first Area
        polygon = [
            {
                "lat" : 0,
                "lon" : 0,
                "altitude" : 0
            }, {
                "lat" : 2,
                "lon" : 0,
                "altitude" : 1
            }, {
                "lat" : 2,
                "lon" : 2,
                "altitude" : 2
            }, {
                "lat" : 0,
                "lon" : 2,
                "altitude" : 3
            }
        ]

        # first not found because no elements is stores
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/intersection',
            method='POST',
            headers=headers,
            data=json.dumps(polygon),
            content_type='application/json')
        self.assertStatus(response, HTTPStatus.NOT_FOUND, 'Response body is : ' + response.data.decode('utf-8'))

        # check when name exist exist =>

        # step1) add an entries
        # step2) check if I can get the entry via api
        # step3) check if nothing is found but something is stored
        self._addAreas()
        areas = getAreas()
        self.assertEqual(len(areas), 2)

        # step 2 - should get the the first Area
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/intersection',
            method='POST',
            headers=headers,
            data=json.dumps(polygon),
            content_type='application/json')
        self.assert200(response,'Response body is : ' + response.data.decode('utf-8'))

        result_areas = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(result_areas), 1)
        self.assertEqual(result_areas[0]['name'], 'Luigi Pirelli')

        # step 3: set a polygon that do not intersect
        polygon = [ {
            "lat" : 4,
            "lon" : 4,
            "altitude" : 1
            }, 
            {
                "lat" : 5,
                "lon" : 4,
                "altitude" : 2
            },
            {
                "lat" : 5,
                "lon" : 5,
                "altitude" : 3
            },
            {
                "lat" : 4,
                "lon" : 5,
                "altitude" : 4
            } 
        ]
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/intersection',
            method='POST',
            headers=headers,
            data=json.dumps(polygon),
            content_type='application/json')
        self.assertStatus(response, HTTPStatus.NOT_FOUND, 'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
