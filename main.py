  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)