# coding: utf-8

from __future__ import absolute_import
import unittest
import sys
from flask import json
from six import BytesIO
import json
from http import HTTPStatus

from openapi_server.models.area import Area  # noqa: E501
from openapi_server.test import BaseTestCase
from openapi_server.data.areas import getAreas, setAreas # noqa: E501

class TestModificationController(BaseTestCase):
    """ModificationController integration test stubs"""

    def test_add_area(self):
        """Test case for add_area

        Add new/modify Area resource
        """
        # reset area
        setAreas({})
        areas = getAreas()
        self.assertEqual(len(areas), 0)

        area = {
  "date" : "2021-04-17",
  "name" : "Luigi Pirelli",
  "poly" : [ {
    "lat" : 43.111,
    "lon" : -8.111,
    "altitude" : 77.1
  }, {
    "lat" : 43.222,
    "lon" : -8.222,
    "altitude" : 77.2
  }, {
    "lat" : 43.333,
    "lon" : -8.333,
    "altitude" : 77.3
  } ],
  "props" : {
    "a_string_value" : "Hello!",
    "an_number_value" : "1111.222"
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

        self.assertEqual(len(areas), 1)
        self.assertTrue(area['name'] in areas.keys())
        self.assertEqual(areas[area['name']].to_dict(), area)

        return None

    def test_delete_are_by_name(self):
        """Test case for delete_are_by_name

        Delete a Area resource by name.
        """
        # first add an element with name 'Luigi Pirelli'
        self.test_add_area()
        areas = getAreas()
        self.assertEqual(len(areas), 1)

        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/{name}'.format(name='Luigi Pirelli'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        self.assertEqual(len(areas), 0)

    def test_delete_are_by_not_existent_name(self):
        """Test case for delete_are_by_name in case Name does not exist
        """
        # first add an element with name 'Luigi Pirelli'
        self.test_add_area()
        areas = getAreas()
        self.assertEqual(len(areas), 1)

        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/{name}'.format(name='a not existent name'),
            method='DELETE',
            headers=headers)
        self.assertStatus(response, HTTPStatus.NOT_FOUND, 'Response body is : ' + response.data.decode('utf-8'))
        # self.assert200(response,
        #                'Response body is : ' + response.data.decode('utf-8'))

        # no chenges
        self.assertEqual(len(areas), 1)


if __name__ == '__main__':
    unittest.main()
