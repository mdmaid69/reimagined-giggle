  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import os
  def split_path(path):
        return os.path.split(path)