  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)