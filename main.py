import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)