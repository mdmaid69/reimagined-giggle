import json
print(json.dumps({"name": "John", "age": 30}))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)