# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.point3_d_dict import Point3DDict
import re
from openapi_server import util

from openapi_server.models.point3_d_dict import Point3DDict  # noqa: E501
import re  # noqa: E501

class Area(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, date=None, props=None, poly=None):  # noqa: E501
        """Area - a model defined in OpenAPI

        :param name: The name of this Area.  # noqa: E501
        :type name: str
        :param date: The date of this Area.  # noqa: E501
        :type date: str
        :param props: The props of this Area.  # noqa: E501
        :type props: Dict[str, str]
        :param poly: The poly of this Area.  # noqa: E501
        :type poly: List[Point3DDict]
        """
        self.openapi_types = {
            'name': str,
            'date': str,
            'props': Dict[str, str],
            'poly': List[Point3DDict]
        }

        self.attribute_map = {
            'name': 'name',
            'date': 'date',
            'props': 'props',
            'poly': 'poly'
        }

        self._name = name
        self._date = date
        self._props = props
        self._poly = poly

    @classmethod
    def from_dict(cls, dikt) -> 'Area':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Area of this Area.  # noqa: E501
        :rtype: Area
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Area.


        :return: The name of this Area.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Area.


        :param name: The name of this Area.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def date(self):
        """Gets the date of this Area.

        Custom date  # noqa: E501

        :return: The date of this Area.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Area.

        Custom date  # noqa: E501

        :param date: The date of this Area.
        :type date: str
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501
        if date is not None and not re.search(r'^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$', date):  # noqa: E501
            raise ValueError("Invalid value for `date`, must be a follow pattern or equal to `/^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/`")  # noqa: E501

        self._date = date

    @property
    def props(self):
        """Gets the props of this Area.


        :return: The props of this Area.
        :rtype: Dict[str, str]
        """
        return self._props

    @props.setter
    def props(self, props):
        """Sets the props of this Area.


        :param props: The props of this Area.
        :type props: Dict[str, str]
        """
        if props is None:
            raise ValueError("Invalid value for `props`, must not be `None`")  # noqa: E501

        self._props = props

    @property
    def poly(self):
        """Gets the poly of this Area.

        Polygon not closed coordinates.  # noqa: E501

        :return: The poly of this Area.
        :rtype: List[Point3DDict]
        """
        return self._poly

    @poly.setter
    def poly(self, poly):
        """Sets the poly of this Area.

        Polygon not closed coordinates.  # noqa: E501

        :param poly: The poly of this Area.
        :type poly: List[Point3DDict]
        """
        if poly is None:
            raise ValueError("Invalid value for `poly`, must not be `None`")  # noqa: E501
        if poly is not None and len(poly) < 3:
            raise ValueError("Invalid value for `poly`, number of items must be greater than or equal to `3`")  # noqa: E501

        self._poly = poly
