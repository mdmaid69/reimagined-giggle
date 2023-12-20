  import os
  def delete_file(file_name):
        os.remove(file_name)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)