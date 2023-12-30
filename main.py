import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value