import json
print(json.dumps({"name": "John", "age": 30}))
  import os
  def get_base_name(path):
        return os.path.basename(path)