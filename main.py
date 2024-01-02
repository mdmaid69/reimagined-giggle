  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)