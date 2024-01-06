import random
def roll_die():
        return random.randint(1, 6)
import json
def read_from_json(json_string):
        return json.loads(json_string)