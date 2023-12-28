  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import json
print(json.dumps({"name": "John", "age": 30}))