import logging
def log_message(message):
        logging.info(message)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)