  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import os
  def split_path(path):
        return os.path.split(path)