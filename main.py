  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)