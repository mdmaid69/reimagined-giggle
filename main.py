  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)