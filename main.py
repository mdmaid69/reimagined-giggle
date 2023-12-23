import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
from collections import Counter
print(Counter("hello world"))