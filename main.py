  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)