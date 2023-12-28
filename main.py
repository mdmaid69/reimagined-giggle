import getpass
def get_username():
        return getpass.getuser()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)