  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)