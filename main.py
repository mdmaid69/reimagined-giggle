  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)