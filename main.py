  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)