  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import json
def convert_to_json(data):
        return json.dumps(data)