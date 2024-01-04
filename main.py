  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)