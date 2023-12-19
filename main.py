import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)