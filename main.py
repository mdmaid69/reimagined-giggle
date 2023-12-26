  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import platform
def get_python_version():
        return platform.python_version()