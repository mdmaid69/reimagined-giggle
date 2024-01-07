import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import os
  def split_path(path):
        return os.path.split(path)