  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)