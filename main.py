  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import json
def convert_to_json(data):
        return json.dumps(data)