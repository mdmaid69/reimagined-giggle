  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)