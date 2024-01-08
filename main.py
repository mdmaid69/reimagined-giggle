import math
def calculate_absolute_value(x):
        return math.fabs(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)