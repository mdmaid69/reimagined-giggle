import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import json
def read_from_json(json_string):
        return json.loads(json_string)