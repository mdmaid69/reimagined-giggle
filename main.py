  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import json
print(json.dumps({"name": "John", "age": 30}))