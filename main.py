  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)