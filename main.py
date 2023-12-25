  import os
  def delete_file(file_name):
        os.remove(file_name)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)