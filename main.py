  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)