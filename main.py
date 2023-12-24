  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import os
def change_working_directory(path):
        os.chdir(path)