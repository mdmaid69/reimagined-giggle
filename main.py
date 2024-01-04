def calculate_power(work, time):
        return work / time
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)