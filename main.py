import json
def read_from_json(json_string):
        return json.loads(json_string)
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns