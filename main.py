import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
n = 10
print("Powers of 2:", [2**x for x in range(n)])