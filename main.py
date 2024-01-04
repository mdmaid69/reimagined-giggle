  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import json
print(json.dumps({"name": "John", "age": 30}))