import re
print(re.match("h.*o", "hello world"))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)