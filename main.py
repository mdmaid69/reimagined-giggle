  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import json
def read_from_json(json_string):
        return json.loads(json_string)