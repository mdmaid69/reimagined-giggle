import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)