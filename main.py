  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)