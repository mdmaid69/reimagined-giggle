import json
def read_from_json(json_string):
        return json.loads(json_string)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])