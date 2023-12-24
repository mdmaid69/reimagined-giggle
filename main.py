  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)