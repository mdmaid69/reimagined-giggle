  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)