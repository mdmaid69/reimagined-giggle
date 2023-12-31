  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)