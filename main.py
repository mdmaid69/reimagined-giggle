  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)