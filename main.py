  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)