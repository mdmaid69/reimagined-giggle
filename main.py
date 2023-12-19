import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)