  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import json
def read_from_json(json_string):
        return json.loads(json_string)