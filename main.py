import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)