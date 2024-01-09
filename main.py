import random
print(random.randint(0, 100))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)