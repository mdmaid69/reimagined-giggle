n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)