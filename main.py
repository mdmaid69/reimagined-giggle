  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import os
  def get_current_directory():
        return os.getcwd()