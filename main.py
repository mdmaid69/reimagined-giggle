import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)