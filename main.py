import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)