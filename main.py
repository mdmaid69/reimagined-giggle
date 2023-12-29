import json
def convert_to_json(data):
        return json.dumps(data)
n = 10
print("Square numbers:", [x**2 for x in range(n)])