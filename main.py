import random
def generate_random_choice(choices):
        return random.choice(choices)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)