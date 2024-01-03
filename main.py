import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def iterate_over_array(array):
        for item in array:
        print(item)