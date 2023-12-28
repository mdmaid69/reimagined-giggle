  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)