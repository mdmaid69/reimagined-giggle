import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"