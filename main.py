import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import json
print(json.dumps({"name": "John", "age": 30}))