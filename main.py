  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import json
def convert_to_json(data):
        return json.dumps(data)