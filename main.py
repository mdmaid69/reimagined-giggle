import json
print(json.dumps({"name": "John", "age": 30}))
import json
def read_from_json(json_string):
        return json.loads(json_string)