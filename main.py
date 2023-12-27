  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)