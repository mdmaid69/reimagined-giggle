import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)