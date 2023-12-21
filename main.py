import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)