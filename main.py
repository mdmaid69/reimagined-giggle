import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)