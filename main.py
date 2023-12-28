  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)