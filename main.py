  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)