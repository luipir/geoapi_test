import connexion
import six

from openapi_server.models.area import Area  # noqa: E501
from openapi_server import util


def add_area(area=None):  # noqa: E501
    """Add new/modify Area resource

    Add a new Area resource or modify existing if unique name already exist  # noqa: E501

    :param area: Area resource to add/substitute
    :type area: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        area = Area.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_are_by_name(name):  # noqa: E501
    """Delete a Area resource by name.

    Delete a Area resource by name.  # noqa: E501

    :param name: resource unique name
    :type name: str

    :rtype: List[Area]
    """
    return 'do some magic!'