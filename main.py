  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import json
def read_from_json(json_string):
        return json.loads(json_string)