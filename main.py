import json
print(json.dumps({"name": "John", "age": 30}))
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)