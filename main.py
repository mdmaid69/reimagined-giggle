  import os
  def split_path(path):
        return os.path.split(path)
import json
def read_from_json(json_string):
        return json.loads(json_string)