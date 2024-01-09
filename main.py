import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)