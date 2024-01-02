  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)