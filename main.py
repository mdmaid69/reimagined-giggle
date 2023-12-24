  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import json
print(json.dumps({"name": "John", "age": 30}))