n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import json
def read_from_json(json_string):
        return json.loads(json_string)