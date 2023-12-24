  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import os
def get_environment_variable(var):
        return os.getenv(var)