  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import json
def convert_to_json(data):
        return json.dumps(data)