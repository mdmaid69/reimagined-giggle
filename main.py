for i in range(5):
        print(i)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)