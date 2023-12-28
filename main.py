import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def split_path(path):
        return os.path.split(path)