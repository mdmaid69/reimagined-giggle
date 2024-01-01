  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)