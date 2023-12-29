import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)