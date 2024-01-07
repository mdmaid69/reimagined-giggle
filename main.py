  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)