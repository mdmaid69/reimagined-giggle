  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)