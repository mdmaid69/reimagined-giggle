  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)