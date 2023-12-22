import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)