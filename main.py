import collections
def create_user_list():
        return collections.UserList()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)