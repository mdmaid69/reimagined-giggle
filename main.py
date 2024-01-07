  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import json
def read_from_json(json_string):
        return json.loads(json_string)