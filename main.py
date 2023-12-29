  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import json
print(json.dumps({"name": "John", "age": 30}))