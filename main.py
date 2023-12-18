import json
def read_from_json(json_string):
        return json.loads(json_string)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)