import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import re
def split_string(pattern, string):
        return re.split(pattern, string)