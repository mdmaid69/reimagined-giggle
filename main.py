import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def sort_numbers(numbers):
        return sorted(numbers)