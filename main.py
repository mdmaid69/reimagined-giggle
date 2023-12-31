  import os
  def get_current_working_directory():
        return os.getcwd()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)