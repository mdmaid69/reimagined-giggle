i = 0
while i < 5:
        print(i)
        i += 1
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)