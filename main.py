  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)