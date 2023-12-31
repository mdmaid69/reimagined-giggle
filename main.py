  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import json
print(json.dumps({"name": "John", "age": 30}))