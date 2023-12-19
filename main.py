import json
print(json.dumps({"name": "John", "age": 30}))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)