import json
def convert_to_json(data):
        return json.dumps(data)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])