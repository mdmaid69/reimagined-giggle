import getpass
def get_username():
        return getpass.getuser()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)