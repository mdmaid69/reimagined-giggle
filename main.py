  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import json
print(json.dumps({"name": "John", "age": 30}))