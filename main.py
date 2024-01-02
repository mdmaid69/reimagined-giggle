  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import json
def read_from_json(json_string):
        return json.loads(json_string)