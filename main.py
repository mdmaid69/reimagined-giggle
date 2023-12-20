import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)