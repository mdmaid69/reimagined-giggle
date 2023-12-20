import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)