import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)