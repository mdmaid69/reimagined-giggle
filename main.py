import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)