  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import json
def convert_to_json(data):
        return json.dumps(data)