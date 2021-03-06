import connexion
import six
import logging
from flask import abort
from http import HTTPStatus

# from shapely.geometry import Polygon

from openapi_server.models.area import Area  # noqa: E501
from openapi_server.data.areas import getAreas, setAreas  # noqa: E501

log = logging.getLogger(__name__)

def add_area(area=None):  # noqa: E501
    """Add new/modify Area resource

    Add a new Area resource or modify existing if unique name already exist  # noqa: E501

    :param area: Area resource to add/substitute
    :type area: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        area = Area.from_dict(connexion.request.get_json())  # noqa: E501

        log.debug('Storing area: {}'.format(area))
        areas = getAreas()
        areas[area.name] = area
        setAreas(areas)
        # log.debug("Stored areas: {}".format(areas[area['name']].name))

    return None, HTTPStatus.NO_CONTENT


def delete_are_by_name(name):  # noqa: E501
    """Delete a Area resource by name.

    Delete a Area resource by name.  # noqa: E501

    :param name: resource unique name
    :type name: str

    :rtype: List[Area]
    """
    areas = getAreas()
    if areas.pop(name, None) is None:
        abort(HTTPStatus.NOT_FOUND)

    return areas, HTTPStatus.OK
