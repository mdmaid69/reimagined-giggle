import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)