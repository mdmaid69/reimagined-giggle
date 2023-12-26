import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import json
def read_from_json(json_string):
        return json.loads(json_string)