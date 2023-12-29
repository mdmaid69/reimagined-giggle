n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)