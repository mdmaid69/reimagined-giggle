  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)