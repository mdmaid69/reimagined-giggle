  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)