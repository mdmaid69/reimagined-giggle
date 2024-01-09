  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import logging
def log_message(message):
        logging.info(message)