  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import json
print(json.dumps({"name": "John", "age": 30}))