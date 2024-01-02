import json
def read_from_json(json_string):
        return json.loads(json_string)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b