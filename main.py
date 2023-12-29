import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import re
def split_string(pattern, string):
        return re.split(pattern, string)