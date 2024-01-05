import json
def read_from_json(json_string):
        return json.loads(json_string)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))