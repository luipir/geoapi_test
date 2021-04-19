# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.area import Area
from openapi_client.model.point3_d_dict import Point3DDict
from openapi_client.model.polygon import Polygon
from openapi_client.model.props import Props
