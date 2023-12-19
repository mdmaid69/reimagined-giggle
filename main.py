import json
def convert_to_json(data):
        return json.dumps(data)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)