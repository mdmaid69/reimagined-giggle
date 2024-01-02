  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import json
def read_from_json(json_string):
        return json.loads(json_string)