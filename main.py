import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value