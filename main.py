  import os
  def get_current_working_directory():
        return os.getcwd()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)