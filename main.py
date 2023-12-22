import getpass
def get_username():
        return getpass.getuser()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)