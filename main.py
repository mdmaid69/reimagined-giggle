import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)