  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import json
print(json.dumps({"name": "John", "age": 30}))