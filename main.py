  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)