  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import json
print(json.dumps({"name": "John", "age": 30}))