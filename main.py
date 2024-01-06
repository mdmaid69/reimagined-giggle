import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def get_base_name(path):
        return os.path.basename(path)