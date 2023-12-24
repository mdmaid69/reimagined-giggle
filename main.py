import random
def generate_random_choice(choices):
        return random.choice(choices)
import json
def read_from_json(json_string):
        return json.loads(json_string)