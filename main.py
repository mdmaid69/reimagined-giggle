import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)