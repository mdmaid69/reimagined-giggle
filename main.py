import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)