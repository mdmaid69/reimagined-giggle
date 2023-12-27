n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)