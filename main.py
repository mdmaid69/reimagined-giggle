  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import json
def read_from_json(json_string):
        return json.loads(json_string)