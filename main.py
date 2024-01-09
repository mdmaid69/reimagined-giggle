import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)