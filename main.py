  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)