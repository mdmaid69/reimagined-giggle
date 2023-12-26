import json
print(json.dumps({"name": "John", "age": 30}))
  import os
  def delete_file(file_name):
        os.remove(file_name)