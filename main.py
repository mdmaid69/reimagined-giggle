numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)