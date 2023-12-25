  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)