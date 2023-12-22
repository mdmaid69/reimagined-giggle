import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)