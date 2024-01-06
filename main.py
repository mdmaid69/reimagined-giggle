  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import json
def read_from_json(json_string):
        return json.loads(json_string)