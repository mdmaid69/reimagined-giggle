  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import json
def convert_to_json(data):
        return json.dumps(data)