  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)