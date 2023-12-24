  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)