  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import json
def convert_to_json(data):
        return json.dumps(data)