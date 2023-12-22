import json
def read_from_json(json_string):
        return json.loads(json_string)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value