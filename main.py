import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import random
print(random.randint(0, 100))