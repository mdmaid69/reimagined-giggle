  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import json
def read_from_json(json_string):
        return json.loads(json_string)