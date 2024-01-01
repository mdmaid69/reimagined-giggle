import os
def get_environment_variable(var):
        return os.getenv(var)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)