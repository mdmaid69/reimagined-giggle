import json
def read_from_json(json_string):
        return json.loads(json_string)
n = 10
print("Powers of 2:", [2**x for x in range(n)])