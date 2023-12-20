  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import json
def read_from_json(json_string):
        return json.loads(json_string)