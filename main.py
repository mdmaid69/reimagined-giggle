  import os
  def get_base_name(path):
        return os.path.basename(path)
import json
def read_from_json(json_string):
        return json.loads(json_string)