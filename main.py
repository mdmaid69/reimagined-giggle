import json
print(json.dumps({"name": "John", "age": 30}))
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]