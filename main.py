  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)