import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)