  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import os
  def delete_file(file_name):
        os.remove(file_name)