  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)