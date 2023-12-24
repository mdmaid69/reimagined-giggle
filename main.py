import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)