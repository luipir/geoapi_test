# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.area import Area  # noqa: E501
from openapi_server.test import BaseTestCase


class TestModificationController(BaseTestCase):
    """ModificationController integration test stubs"""

    def test_add_area(self):
        """Test case for add_area

        Add new/modify Area resource
        """
        area = {
  "date" : "2021-04-17T00:00:00.000+0000",
  "area" : [ [ -8.226312, 43.29702, 77 ], [ -8.226312, 43.29702, 77 ] ],
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

    def test_delete_are_by_name(self):
        """Test case for delete_are_by_name

        Delete a Area resource by name.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/luipir/geo_test/1.0.0/areas/{name}'.format(name='name_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
