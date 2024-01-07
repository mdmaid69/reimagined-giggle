  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import json
print(json.dumps({"name": "John", "age": 30}))