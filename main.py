  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)