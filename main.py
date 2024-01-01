  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)