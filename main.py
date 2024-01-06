import logging
def log_message(message):
        logging.info(message)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)