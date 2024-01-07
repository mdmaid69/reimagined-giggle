  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)