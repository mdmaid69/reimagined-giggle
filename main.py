import collections
def create_user_string():
        return collections.UserString()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)