from collections import Counter
print(Counter("hello world"))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)