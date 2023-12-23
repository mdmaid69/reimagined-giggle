  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import json
print(json.dumps({"name": "John", "age": 30}))