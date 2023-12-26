  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)