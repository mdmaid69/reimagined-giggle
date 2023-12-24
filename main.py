import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)