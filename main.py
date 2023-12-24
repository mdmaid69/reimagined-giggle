import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)