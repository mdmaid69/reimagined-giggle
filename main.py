i = 0
while i < 5:
        print(i)
        i += 1
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)