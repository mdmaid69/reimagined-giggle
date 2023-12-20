import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)