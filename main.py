import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import json
def convert_to_json(data):
        return json.dumps(data)