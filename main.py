def square_number(x):
        return x**2
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)