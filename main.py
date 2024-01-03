import platform
def get_os_info():
        return platform.uname()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)