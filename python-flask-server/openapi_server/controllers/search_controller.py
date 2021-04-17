import connexion
import six

from openapi_server.models.area import Area  # noqa: E501
from openapi_server import util


def delete_are_by_name(name):  # noqa: E501
    """Delete a Area resource by name.

    Delete a Area resource by name.  # noqa: E501

    :param name: resource unique name
    :type name: str

    :rtype: List[Area]
    """
    return 'do some magic!'
