  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)