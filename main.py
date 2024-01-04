import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)