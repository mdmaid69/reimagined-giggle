  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)