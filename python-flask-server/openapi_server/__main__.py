#!/usr/bin/env python3

import connexion
import os
import logging

from openapi_server import encoder

logname = os.path.normpath(os.path.join(os.path.dirname(__file__), 'log.txt'))
logging.basicConfig(filename=logname,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'GEO_Test API'},
                pythonic_params=True)

    app.run(port=8080)

if __name__ == '__main__':
    main()
