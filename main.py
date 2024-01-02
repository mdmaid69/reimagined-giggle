import logging
def log_message(message):
        logging.info(message)
import json
def read_from_json(json_string):
        return json.loads(json_string)