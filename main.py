  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)