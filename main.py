import json
def convert_to_json(data):
        return json.dumps(data)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])