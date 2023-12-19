  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import json
print(json.dumps({"name": "John", "age": 30}))