# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.area import Area  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSearchController(BaseTestCase):
    """SearchController integration test stubs"""

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
