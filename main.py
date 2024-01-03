  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)