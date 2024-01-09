import json
def convert_to_json(data):
        return json.dumps(data)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")