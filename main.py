import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import json
def read_from_json(json_string):
        return json.loads(json_string)