  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)