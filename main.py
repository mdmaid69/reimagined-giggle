print([x**2 for x in range(10)])
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)