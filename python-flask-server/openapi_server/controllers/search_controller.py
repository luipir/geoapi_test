import connexion
import six

from openapi_server.models.area import Area  # noqa: E501
from openapi_server.models.props import Props  # noqa: E501
from openapi_server import util


def get_area_by_date(date):  # noqa: E501
    """Retrieve a Area with a specified data.

    Retrieve a Area resource by date.  # noqa: E501

    :param date: Get all resources containing the name
    :type date: str

    :rtype: List[Area]
    """
    return 'do some magic!'


def get_area_by_name(name):  # noqa: E501
    """Retrieve a Area resource by unique name.

    Retrieve a Area resource by unique name.  # noqa: E501

    :param name: resource unique name
    :type name: str

    :rtype: List[Area]
    """
    return 'do some magic!'


def get_area_by_properties(props=None):  # noqa: E501
    """Retrieve a Area with a specified data set of properties.

    Retrieve a Area resource by properties dict.  # noqa: E501

    :param props: Area to retrieve with matching properties
    :type props: dict | bytes

    :rtype: List[Area]
    """
    if connexion.request.is_json:
        props = Props.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_intersected(request_body=None):  # noqa: E501
    """Retrieve a Area inteersecting posted polygon.

    Retrieve intersecting Area resources   # noqa: E501

    :param request_body: Polygon to retrieve intersecting Area resources
    :type request_body: List[]

    :rtype: List[Area]
    """
    return 'do some magic!'


def get_intersection(request_body=None):  # noqa: E501
    """Retrieve Area inside input polygon.

    Retrieve Area inside input polygon  # noqa: E501

    :param request_body: Polygon to retrieve inner Area resources
    :type request_body: List[]

    :rtype: List[Area]
    """
    return 'do some magic!'
