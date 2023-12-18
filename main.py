  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import platform
def get_os_info():
        return platform.uname()