import json
def read_from_json(json_string):
        return json.loads(json_string)
n = 10
print("Square numbers:", [x**2 for x in range(n)])