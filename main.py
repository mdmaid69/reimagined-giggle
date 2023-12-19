for i in range(5):
        print(i)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)