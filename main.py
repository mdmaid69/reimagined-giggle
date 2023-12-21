  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import json
print(json.dumps({"name": "John", "age": 30}))