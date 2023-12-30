def find_max(numbers):
        return max(numbers)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)