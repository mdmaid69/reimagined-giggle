import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)