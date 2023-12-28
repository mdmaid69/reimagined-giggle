import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import logging
def log_message(message):
        logging.info(message)