  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)