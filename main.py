import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import json
def convert_to_json(data):
        return json.dumps(data)