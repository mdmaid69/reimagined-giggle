import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)