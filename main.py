  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import json
def read_from_json(json_string):
        return json.loads(json_string)