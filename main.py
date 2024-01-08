import os
def remove_directory(path):
        os.rmdir(path)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)