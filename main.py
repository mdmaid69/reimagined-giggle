import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import json
def convert_to_json(data):
        return json.dumps(data)