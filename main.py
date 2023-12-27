import json
def convert_to_json(data):
        return json.dumps(data)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])