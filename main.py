import json
def convert_to_json(data):
        return json.dumps(data)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)