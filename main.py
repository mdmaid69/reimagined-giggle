  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)