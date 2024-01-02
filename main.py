  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)