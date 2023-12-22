n = 10
print("Square numbers:", [x**2 for x in range(n)])
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)