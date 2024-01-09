  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)