import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)