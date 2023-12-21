  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)