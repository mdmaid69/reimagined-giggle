  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)