import json
print(json.dumps({"name": "John", "age": 30}))
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid