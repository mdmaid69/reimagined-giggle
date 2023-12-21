  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)