def calculate_average(lst):
        return sum(lst) / len(lst)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)