import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]