import json
def read_from_json(json_string):
        return json.loads(json_string)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]