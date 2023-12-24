  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)