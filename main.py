  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)