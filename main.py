import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)