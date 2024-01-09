numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)