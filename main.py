import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)