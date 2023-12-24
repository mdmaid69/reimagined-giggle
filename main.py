  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)