  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import json
def read_from_json(json_string):
        return json.loads(json_string)