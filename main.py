import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)