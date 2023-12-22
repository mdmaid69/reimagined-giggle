import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import re
def split_string(pattern, string):
        return re.split(pattern, string)