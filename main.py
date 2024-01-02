  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)