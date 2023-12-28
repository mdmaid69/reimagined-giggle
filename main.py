  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)