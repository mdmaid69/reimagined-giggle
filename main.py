  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"