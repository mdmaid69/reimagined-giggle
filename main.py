import json
def convert_to_json(data):
        return json.dumps(data)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)