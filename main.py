import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import os
  def split_path(path):
        return os.path.split(path)