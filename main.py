import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))