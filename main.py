  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import json
print(json.dumps({"name": "John", "age": 30}))