  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)