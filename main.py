  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)