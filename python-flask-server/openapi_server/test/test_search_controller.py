# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.area import Area  # noqa: E501
from openapi_server.models.point3_d_dict import Point3DDict  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSearchController(BaseTestCase):
    """SearchController integration test stubs"""

    def test_get_area_by_date(self):
        """Test case for get_area_by_date

        Retrieve a Area with a specified data.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/date/{date}'.format(date='2021-01-30'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_area_by_name(self):
        """Test case for get_area_by_name

        Retrieve a Area resource by unique name.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_area_by_properties(self):
        """Test case for get_area_by_properties

        Retrieve a Area with a specified data set of properties.
        """
        props = {
  "a_string_value" : "Hello!",
  "an_number_value" : "1111.222"
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
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_intersect(self):
        """Test case for get_intersect

        Retrieve a Area inteersecting posted polygon.
        """
        polygon = [ {
            "lat" : 43.29702,   
            "lon" : -8.226312,
            "altitude" : 77
            }, {
                "lat" : 43.29702,
                "lon" : -8.226312,
                "altitude" : 77
            }, {
                "lat" : 43.29702,
                "lon" : -8.226312,
                "altitude" : 77
            } 
        ]
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
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_intersection(self):
        """Test case for get_intersection

        Retrieve Area inside input polygon.
        """
        polygon = [ {
            "lat" : 43.29702,   
            "lon" : -8.226312,
            "altitude" : 77
            }, {
                "lat" : 43.29702,
                "lon" : -8.226312,
                "altitude" : 77
            }, {
                "lat" : 43.29702,
                "lon" : -8.226312,
                "altitude" : 77
            } 
        ]
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
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
