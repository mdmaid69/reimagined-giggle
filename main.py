  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import json
def convert_to_json(data):
        return json.dumps(data)