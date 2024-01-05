  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)