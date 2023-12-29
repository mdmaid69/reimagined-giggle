import re
print(re.match("h.*o", "hello world"))
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)