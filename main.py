  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)