n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import json
def read_from_json(json_string):
        return json.loads(json_string)