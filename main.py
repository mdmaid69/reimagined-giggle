import getpass
def get_username():
        return getpass.getuser()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)