  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)