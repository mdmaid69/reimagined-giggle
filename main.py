import os
def get_current_working_directory():
        return os.getcwd()
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)