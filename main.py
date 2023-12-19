  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)