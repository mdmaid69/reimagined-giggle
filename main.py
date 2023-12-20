import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)