  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)