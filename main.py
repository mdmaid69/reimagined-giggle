  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)