  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import json
print(json.dumps({"name": "John", "age": 30}))