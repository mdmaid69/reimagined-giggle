  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)