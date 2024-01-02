import json
def read_from_json(json_string):
        return json.loads(json_string)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)