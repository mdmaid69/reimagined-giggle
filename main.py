import getpass
def get_username():
        return getpass.getuser()
import json
def read_from_json(json_string):
        return json.loads(json_string)