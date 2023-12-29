import json
def convert_to_json(data):
        return json.dumps(data)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)