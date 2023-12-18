import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)