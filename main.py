  import os
  def delete_file(file_name):
        os.remove(file_name)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)