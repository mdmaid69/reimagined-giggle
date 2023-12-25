import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import json
def convert_to_json(data):
        return json.dumps(data)