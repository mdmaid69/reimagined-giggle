  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import json
print(json.dumps({"name": "John", "age": 30}))