import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)