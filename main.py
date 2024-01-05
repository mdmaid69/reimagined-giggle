import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import json
print(json.dumps({"name": "John", "age": 30}))