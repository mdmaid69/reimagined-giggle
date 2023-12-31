  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)