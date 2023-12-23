import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)