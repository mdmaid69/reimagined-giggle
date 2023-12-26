  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import json
def convert_to_json(data):
        return json.dumps(data)