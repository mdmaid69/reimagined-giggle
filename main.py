  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import json
print(json.dumps({"name": "John", "age": 30}))