import json
print(json.dumps({"name": "John", "age": 30}))
import logging
def setup_logging(level):
        logging.basicConfig(level=level)