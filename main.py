  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import json
print(json.dumps({"name": "John", "age": 30}))