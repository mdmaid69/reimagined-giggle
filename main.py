  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import json
print(json.dumps({"name": "John", "age": 30}))