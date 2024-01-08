import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])