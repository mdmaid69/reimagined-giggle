  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)