  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)