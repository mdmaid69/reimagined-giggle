import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)