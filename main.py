  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)