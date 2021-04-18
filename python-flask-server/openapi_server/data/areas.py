from typing import Dict
from openapi_server.models.area import Area  # noqa: E501

# where to store Areas basing on name
__areas: Dict[str, Area] = {}

def getAreas():
    return __areas

def setAreas(areas: Dict[str, Area]):
    global __areas
    __areas = areas