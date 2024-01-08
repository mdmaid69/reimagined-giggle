  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import json
def convert_to_json(data):
        return json.dumps(data)