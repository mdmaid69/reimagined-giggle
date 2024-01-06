  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import getpass
def get_username():
        return getpass.getuser()