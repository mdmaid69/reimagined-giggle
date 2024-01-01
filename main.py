  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)