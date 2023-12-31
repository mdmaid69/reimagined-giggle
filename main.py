  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import random
def roll_die():
        return random.randint(1, 6)