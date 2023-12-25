import json
def read_from_json(json_string):
        return json.loads(json_string)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)