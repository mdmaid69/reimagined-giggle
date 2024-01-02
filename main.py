import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)