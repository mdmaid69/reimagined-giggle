import os
def list_files_in_directory(path):
        return os.listdir(path)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)