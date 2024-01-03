import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)