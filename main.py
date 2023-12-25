import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b