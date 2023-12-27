import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)