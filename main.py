import json
print(json.dumps({"name": "John", "age": 30}))
import re
def split_string(pattern, string):
        return re.split(pattern, string)