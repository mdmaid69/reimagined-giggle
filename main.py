  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)