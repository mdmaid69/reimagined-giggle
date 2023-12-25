import random
def generate_random_choice(choices):
        return random.choice(choices)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)