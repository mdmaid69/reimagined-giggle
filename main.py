  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)