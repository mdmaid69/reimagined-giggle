import json
def read_from_json(json_string):
        return json.loads(json_string)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)