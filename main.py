import json
print(json.dumps({"name": "John", "age": 30}))
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)