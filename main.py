  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)