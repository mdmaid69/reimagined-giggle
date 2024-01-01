  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import json
def convert_to_json(data):
        return json.dumps(data)