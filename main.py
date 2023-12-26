n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)