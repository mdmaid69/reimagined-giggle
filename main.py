import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)