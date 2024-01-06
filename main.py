import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)