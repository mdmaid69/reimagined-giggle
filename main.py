  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import json
def convert_to_json(data):
        return json.dumps(data)