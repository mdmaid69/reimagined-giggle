import json
def read_from_json(json_string):
        return json.loads(json_string)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)