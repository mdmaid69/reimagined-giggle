import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)