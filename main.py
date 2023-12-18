import math
def calculate_cosine(x):
        return math.cos(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)