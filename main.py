  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)