import random
def roll_die():
        return random.randint(1, 6)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)