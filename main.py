import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)