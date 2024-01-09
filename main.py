import getpass
def get_username():
        return getpass.getuser()
import json
def convert_to_json(data):
        return json.dumps(data)