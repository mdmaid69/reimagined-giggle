import sys
print(sys.version)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)