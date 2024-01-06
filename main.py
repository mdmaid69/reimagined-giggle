import logging
def log_message(message):
        logging.info(message)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)