import random
def generate_random_number(start, end):
        return random.randint(start, end)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)