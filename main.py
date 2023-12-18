import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)