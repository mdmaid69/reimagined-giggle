  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import json
def convert_to_json(data):
        return json.dumps(data)