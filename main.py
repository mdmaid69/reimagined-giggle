  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import json
def read_from_json(json_string):
        return json.loads(json_string)