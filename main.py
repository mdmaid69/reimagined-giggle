import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])