import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import random
def generate_random_number(start, end):
        return random.randint(start, end)