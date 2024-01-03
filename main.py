import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)