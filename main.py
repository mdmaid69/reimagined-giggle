  import os
  def get_base_name(path):
        return os.path.basename(path)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)