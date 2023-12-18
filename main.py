  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)