import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import json
print(json.dumps({"name": "John", "age": 30}))