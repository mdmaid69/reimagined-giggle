  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)