import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import random
def generate_random_choice(choices):
        return random.choice(choices)