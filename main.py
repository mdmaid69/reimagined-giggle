  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)