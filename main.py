import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def get_current_directory():
        return os.getcwd()