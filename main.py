import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)