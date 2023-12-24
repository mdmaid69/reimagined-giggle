import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import os
  def get_base_name(path):
        return os.path.basename(path)