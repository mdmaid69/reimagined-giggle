import json
print(json.dumps({"name": "John", "age": 30}))
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value