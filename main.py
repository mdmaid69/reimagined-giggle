import json
def read_from_json(json_string):
        return json.loads(json_string)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)