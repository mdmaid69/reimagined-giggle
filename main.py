  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import json
def read_from_json(json_string):
        return json.loads(json_string)