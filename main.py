  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)