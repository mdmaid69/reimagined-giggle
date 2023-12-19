  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)