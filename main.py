  import os
  def delete_file(file_name):
        os.remove(file_name)
import json
def read_from_json(json_string):
        return json.loads(json_string)