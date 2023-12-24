  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)