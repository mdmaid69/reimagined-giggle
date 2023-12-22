import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)