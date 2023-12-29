import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]