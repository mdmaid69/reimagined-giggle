import random
def generate_random_number(start, end):
        return random.randint(start, end)
import json
def read_from_json(json_string):
        return json.loads(json_string)