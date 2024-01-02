import json
def read_from_json(json_string):
        return json.loads(json_string)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])