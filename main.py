import platform
def get_python_version():
        return platform.python_version()
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)