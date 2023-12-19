import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def split_path(path):
        return os.path.split(path)