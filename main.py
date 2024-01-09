import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)