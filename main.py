  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import json
def read_from_json(json_string):
        return json.loads(json_string)