import json
def convert_to_json(data):
        return json.dumps(data)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b