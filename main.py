  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import json
print(json.dumps({"name": "John", "age": 30}))