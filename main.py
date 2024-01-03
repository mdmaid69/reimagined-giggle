  import os
  def get_current_directory():
        return os.getcwd()
import json
def read_from_json(json_string):
        return json.loads(json_string)