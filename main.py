import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import json
def read_from_json(json_string):
        return json.loads(json_string)