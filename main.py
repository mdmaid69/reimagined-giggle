  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)