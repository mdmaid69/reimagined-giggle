n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import json
def read_from_json(json_string):
        return json.loads(json_string)