  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import json
def convert_to_json(data):
        return json.dumps(data)