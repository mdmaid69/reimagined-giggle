n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)