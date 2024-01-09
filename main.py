n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import json
def read_from_json(json_string):
        return json.loads(json_string)