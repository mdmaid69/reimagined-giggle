import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))