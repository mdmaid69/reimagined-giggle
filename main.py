  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]