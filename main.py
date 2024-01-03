import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
from collections import Counter
print(Counter("hello world"))