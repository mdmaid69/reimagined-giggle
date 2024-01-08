import json
def read_from_json(json_string):
        return json.loads(json_string)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])