n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import json
def convert_to_json(data):
        return json.dumps(data)