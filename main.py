import json
print(json.dumps({"name": "John", "age": 30}))
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)