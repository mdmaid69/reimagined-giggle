  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)