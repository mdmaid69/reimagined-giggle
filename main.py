  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import json
print(json.dumps({"name": "John", "age": 30}))