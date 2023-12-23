def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)