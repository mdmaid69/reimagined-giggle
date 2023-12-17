  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)