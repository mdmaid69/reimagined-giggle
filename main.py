import re
def split_string(pattern, string):
        return re.split(pattern, string)
import json
def read_from_json(json_string):
        return json.loads(json_string)