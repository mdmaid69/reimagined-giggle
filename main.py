  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import json
def convert_to_json(data):
        return json.dumps(data)