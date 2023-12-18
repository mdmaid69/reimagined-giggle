  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import json
def convert_to_json(data):
        return json.dumps(data)