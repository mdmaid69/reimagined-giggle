  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)