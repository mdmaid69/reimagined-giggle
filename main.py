  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import json
print(json.dumps({"name": "John", "age": 30}))