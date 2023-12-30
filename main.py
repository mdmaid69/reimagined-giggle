  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)