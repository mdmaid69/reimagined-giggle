import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import random
def roll_die():
        return random.randint(1, 6)