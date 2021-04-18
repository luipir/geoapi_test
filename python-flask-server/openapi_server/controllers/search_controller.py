import connexion
import six
import logging

from openapi_server.models.area import Area  # noqa: E501
from openapi_server.models.point3_d_dict import Point3DDict  # noqa: E501
from openapi_server import util
from openapi_server.data.areas import getAreas  # noqa: E501
 
log = logging.getLogger(__name__)

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
    areas = getAreas()
    matched_keys = [val for key, val in areas.items() if name in key]
    results = [areas[key] for key in matched_keys]
    log.debug('Matched: {}'.format(results))
    return 'do some magic!'


def get_area_by_properties(request_body=None):  # noqa: E501
    """Retrieve a Area with a specified data set of properties.

    Retrieve a Area resource by properties dict.  # noqa: E501

    :param request_body: Area to retrieve with matching properties
    :type request_body: Dict[str, str]

    :rtype: List[Area]
    """
    return 'do some magic!'


def get_intersect(point3_d_dict=None):  # noqa: E501
    """Retrieve a Area inteersecting posted polygon.

    Retrieve intersecting Area resources   # noqa: E501

    :param point3_d_dict: Polygon to retrieve intersecting Area resources
    :type point3_d_dict: list | bytes

    :rtype: List[Area]
    """
    if connexion.request.is_json:
        point3_d_dict = [Point3DDict.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def get_intersection(point3_d_dict=None):  # noqa: E501
    """Retrieve Area inside input polygon.

    Retrieve Area inside input polygon  # noqa: E501

    :param point3_d_dict: Polygon to retrieve inner Area resources
    :type point3_d_dict: list | bytes

    :rtype: List[Area]
    """
    if connexion.request.is_json:
        point3_d_dict = [Point3DDict.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
