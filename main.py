  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)