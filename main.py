import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)