  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)