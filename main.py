  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)