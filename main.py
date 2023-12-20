  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import json
def convert_to_json(data):
        return json.dumps(data)