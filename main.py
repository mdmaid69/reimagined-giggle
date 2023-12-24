  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import json
def read_from_json(json_string):
        return json.loads(json_string)