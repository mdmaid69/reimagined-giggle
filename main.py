import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns