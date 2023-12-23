  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import json
def read_from_json(json_string):
        return json.loads(json_string)