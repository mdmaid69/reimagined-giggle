  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import json
def convert_to_json(data):
        return json.dumps(data)