import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink