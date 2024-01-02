  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")