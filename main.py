import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)