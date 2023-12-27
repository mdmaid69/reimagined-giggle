import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))