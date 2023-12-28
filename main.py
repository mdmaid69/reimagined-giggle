import json
print(json.dumps({"name": "John", "age": 30}))
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)