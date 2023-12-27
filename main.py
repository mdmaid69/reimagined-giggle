import json
def convert_to_json(data):
        return json.dumps(data)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)