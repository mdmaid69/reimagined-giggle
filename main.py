  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)