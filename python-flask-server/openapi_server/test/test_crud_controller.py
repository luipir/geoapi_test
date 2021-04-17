# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.area import Area  # noqa: E501
from openapi_server.models.props import Props  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCrudController(BaseTestCase):
    """CrudController integration test stubs"""

    def test_add_area(self):
        """Test case for add_area

        Add new/modify Area resource
        """
        area = {
  "date" : "2021-04-17T00:00:00.000+0000",
  "area" : [ null, null ],
  "name" : "Luigi Pirelli",
  "properties" : {
    "a_string_value" : "Hello!",
    "an_number_value" : 1111.222
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
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_area_by_date(self):
        """Test case for get_area_by_date

        Retrieve a Area with a specified data.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/{date}'.format(date='2021-01-30'),
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
  "an_number_value" : 1111.222
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

    def test_get_intersected(self):
        """Test case for get_intersected

        Retrieve a Area inteersecting posted polygon.
        """
        request_body = None
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/intersect',
            method='POST',
            headers=headers,
            data=json.dumps(request_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_intersection(self):
        """Test case for get_intersection

        Retrieve Area inside input polygon.
        """
        request_body = None
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/intersection',
            method='POST',
            headers=headers,
            data=json.dumps(request_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
